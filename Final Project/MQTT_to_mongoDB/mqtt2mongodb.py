#!/usr/bin/python3

import paho.mqtt.client as mqtt
from pymongo import MongoClient
import re
import datetime
import pprint

from settings import mongodb_url, openhabian_ip, openhabian_user, openhabian_pwd

message = 'ON'

last_node = -1
data_template = {}
last_door_status = ''

# only collect data from dev04, dev48, dev49 and dev50 (battery_voltage, temperature, humidity, pressur    e)
pattern = re.compile(r'home/rfm_gw/nb/node(?P<node>[a-zA-Z0-9]+?)/dev(?P<dev>04|72|4[8-9]|50)')

client = MongoClient(mongodb_url)
db = client.iot_db

# function to return ISOTIME format
def current_time():
	utc_datetime = datetime.datetime.utcnow()
	datestr = utc_datetime.isoformat()
	return datestr+'Z'

def publish_data(payload):
    pprint.pprint(payload, indent=2)
    result = db.home_conditions.insert_one(payload)
    print('MongoDB Result: {0}'.format(result.inserted_id))
    print(result)

def concat_data_msg(node, dev, value, msg_time):
    global last_node
    global data_template
    global last_door_status

    # print('Node: '+str(node)+' Dev:  '+str(dev)+' '+str(value))

    if dev == 72:   # Switch is OPEN, CLOSED, OPENING, CLOSING
        col = 'device%02d'%node
        doordata = {
            'event_time':msg_time,
            'device_id':node,
            'gateway':1,
            'door_status': value.decode('ascii')
            }

        if doordata['door_status'] != last_door_status:
            result = db.doors.insert_one(doordata)
            last_door_status = doordata['door_status']
            print('MongoDB Result doors Collection ({0}): {1}'.format(col, result.inserted_id))
        print(doordata)

    if node != last_node:
        if dev == 48:
            data_template['temperature'] = float(value)
            # temp_data = float(value)
        elif dev == 49:
            data_template['humidity'] = float(value)
            # humidity_data = float(value)
        elif dev == 4:
            data_template['bat_voltage'] = float(value)
            # bat_volt_data = float(value)
        elif dev == 50:
            data_template['pressure'] = float(value)
            data_template['event_time'] = msg_time
            data_template['device_id'] = node
            data_template['gateway'] = 1
            # pressure_data = float(value)
        # if all data values are filled in then send to database (NOT WORKING!)
        # if temp_data != float('nan') and pressure_data != float('nan') and humidity_data != float('nan') and bat_volt_data != float('nan'):
            col = 'device%02d'%node
            result = db[col].insert_one(data_template)
            print('MongoDB Result ({0}): {1}'.format(col, result.inserted_id))
            print(data_template)
            data_template = {}
            # Zero out global values of data so that we do not re-use old data
            last_node = node

def on_connect(mosq, obj, rc):
    print("rc: " + str(rc))

def on_message(mosq, obj, msg):
    global message
    # check for pattern match in message
    m = pattern.search(msg.topic)
    if m:
        #time_now = current_time()
        time_now = datetime.datetime.utcnow()
        # print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
        concat_data_msg(int(m.group('node')), int(m.group('dev')), msg.payload, time_now)

    message = msg.payload

def on_publish(mosq, obj, mid):
    print("mid: " + str(mid))

def on_subscribe(mosq, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

def on_log(mosq, obj, level, string):
    print(string)

if __name__=="__main__":
    mqttc = mqtt.Client()
    # Assign event callbacks
    mqttc.on_message = on_message
    # mqttc.on_connect = on_connect
    mqttc.on_publish = on_publish
    mqttc.on_subscribe = on_subscribe
    # Connect
    mqttc.username_pw_set(openhabian_user,password=openhabian_pwd)
    mqttc.connect(openhabian_ip, 1883,60)

    # Start subscribe, with QoS level 0
    mqttc.subscribe("#", 0)

    # Publish a message
    #mqttc.publish("hello/world", "my message")

    # Continue the network loop, exit when an error occurs
    rc = 0
    while rc == 0:
        rc = mqttc.loop()
