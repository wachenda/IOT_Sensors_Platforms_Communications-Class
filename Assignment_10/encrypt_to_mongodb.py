#!/usr/bin/python3

from Crypto.Cipher import AES
from Crypto import Random
import base64

from pymongo import MongoClient

from settings import pwd, mongodb_url

import datetime


from bme280 import *


sensor = BME280(t_mode=BME280_OSAMPLE_8, p_mode=BME280_OSAMPLE_8, h_mode=BME280_OSAMPLE_8)
BUS = 1
BME280_I2C_ADDR=0x77

client = MongoClient(mongodb_url)
db = client.iot_db

BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS) 
unpad = lambda s : s[:-ord(s[len(s)-1:])]

class AESCipher:
    def __init__( self, key ):
        self.key = key

    def encrypt( self, raw ):
        raw = pad(raw)
        iv = Random.new().read( AES.block_size )
        cipher = AES.new( self.key, AES.MODE_CBC, iv )
        return base64.b64encode( iv + cipher.encrypt( raw ) ) 

    def decrypt( self, enc ):
        enc = base64.b64decode(enc)
        iv = enc[:16]
        cipher = AES.new(self.key, AES.MODE_CBC, iv )
        return unpad(cipher.decrypt( enc[16:] ))

def main():


    aes = AESCipher(pwd)
    temperature = round(sensor.read_temperature_f(),3)
    pressure = round(sensor.read_pressure(),3)
    humidity = round(sensor.read_humidity(),3)
    event_time = datetime.datetime.utcnow()

    print('Temperature: '+str(temperature)+' Pressure: '+str(pressure)+' Humdity: '+str(humidity)+str(event_time))

    data_template = {
            'temperature':aes.encrypt(str(temperature)) , 
            'pressure':aes.encrypt(str(pressure)), 
            'humidity':aes.encrypt(str(humidity)), 
            'event_time':event_time}

    print(data_template)

    result = db.encrypted_results.insert_one(data_template)
    print('MongoDB Insertion Result: '+str(result))
    print()
    time.sleep(1)



if __name__=="__main__":
    while True:
     main()