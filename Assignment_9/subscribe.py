#!/usr/bin/python3

from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub
from pubnub.callbacks import SubscribeCallback

pnconfig = PNConfiguration()

# Need to replace with real pubnub keys to use
pnconfig.subscribe_key = 'sub-c-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'
pnconfig.publish_key = 'pub-c-xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'

pubnub = PubNub(pnconfig)

channel = 'pi-iot'


class Listener(SubscribeCallback):
    def message(self, pubnub, message):
        print('Received PubNub Message:  ', message.message)
        print("Temperature:  %.3f F" %message.message[0])
        print("Pressure    : %.3f hPa" % message.message[1])
        print("Humidity    : %.3f RH"% message.message[2])
        print(message.message[3])
        print()
        

print('Listening...')
pubnub.add_listener(Listener())
pubnub.subscribe().channels(channel).execute()
