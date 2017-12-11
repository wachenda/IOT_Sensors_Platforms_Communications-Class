#!/usr/bin/python3

from Crypto.Cipher import AES
from Crypto import Random
import base64

from pymongo import MongoClient

from settings import pwd, mongodb_url

import datetime


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
    
    documents = db.encrypted_results.find()

    for d in documents:
        data_template = {
                'temperature':aes.decrypt(d['temperature']) , 
                'pressure':aes.decrypt(d['pressure']), 
                'humidity':aes.decrypt(d['humidity']), 
                'event_time':d['event_time']}

        print(data_template)

    
    print()
    



if __name__=="__main__":
    main()