#!/usr/bin/python3
import sys
from pubnub.pubnub import PubNub
from pubnub.pnconfiguration import PNConfiguration
from pubnub.callbacks import SubscribeCallback

import datetime
import atexit

from bme280 import *


sensor = BME280(t_mode=BME280_OSAMPLE_8, p_mode=BME280_OSAMPLE_8, h_mode=BME280_OSAMPLE_8)
BUS = 1
BME280_I2C_ADDR=0x77

# data = {
#         'temperature' : 20., 
#         'humidity' : 50.,
#         'pressure' : 1000.,
#         'eventtime' :''
#         }

#setup
pubconf = PNConfiguration()
# Need to replace with real pubnub keys to use
pubconf.subscribe_key = 'sub-c-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'
pubconf.publish_key = 'pub-c-xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'

pubnub = PubNub(pubconf)

#assign a channel
channel = 'pi-iot'

#callback section
def publish_callback(envelope, status):
    # Check whether request successfully completed or not
    if not status.is_error():
        # Message successfully published to specified channel.
        print("Message Sent")
    else:
        # Handle message publish error. Check 'category' property to find out possible issue
        # because of which request did fail.
        # Request can be resent using: [status retry];
        print("Error Sending!")


def current_time():
	utc_datetime = datetime.datetime.utcnow()
	datestr = utc_datetime.isoformat()
	return datestr+'Z'

def main():

    temperature = round(sensor.read_temperature_f(),3)
    pressure = round(sensor.read_pressure(),3)
    humidity = round(sensor.read_humidity(),3)
    event_time = current_time()
    
    data = [temperature , pressure, humidity, event_time]
    print("Temperature : %.3f deg F" % temperature)
    print("Pressure    : %.3f hPa" % pressure)
    print("Humidity    : %.3f RH"% humidity)
    print(event_time)
    print()
    pubnub.publish().channel(channel).message(data).async(publish_callback)
	
    time.sleep(1)
	
if __name__=="__main__":
	while True:
		main()
