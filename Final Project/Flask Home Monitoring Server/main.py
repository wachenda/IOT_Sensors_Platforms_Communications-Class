#!/usr/bin/python3

from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_pymongo import PyMongo, pymongo
from settings import mongo_dbname, mongodb_url
import datetime
from pytz import timezone

import numpy as np

devices = []

app = Flask(__name__)
Bootstrap(app)

app.config['MONGO_DBNAME'] = mongo_dbname
app.config['MONGO_URI'] = mongodb_url

mongo = PyMongo(app)

@app.route('/')
def index():
    global devices
    devices = []
    device_lst = mongo.db.Device_Name_Mapping.find().sort('_id',pymongo.ASCENDING)
    for i in device_lst:
        devices.append({'col':'device%02d'%int(i['_id']), 'Location':i['Location']})
    output=[]
    for i in devices:
        data = mongo.db[i['col']].find().sort('$natural',pymongo.DESCENDING).limit(1)
        d = data[0]
        output.append({'Location':i['Location'],
                        'Name':i['col'],
                        'Temperature':"%.1f"%d['temperature'],
                        'Pressure':"%.1f"%d['pressure'],
                        'Humidity':"%.1f"%d['humidity'],
                        'Voltage':"%.2f"%d['bat_voltage'],
                        'Event_Time':d['event_time'].astimezone(timezone('US/Pacific')).strftime('%a %-I:%M:%S %p %Z')})
    sorted_output = sorted(output, key=lambda x: x['Event_Time'], reverse=True)
    currenttime = datetime.datetime.now().strftime('%A  %-I:%M:%S %p %Z  %b %-d, %Y')
    return render_template('index_bootstrap.html',devices=sorted_output, currenttime = currenttime)


@app.route('/plot/<string:name>/<string:loc>')
def plot(name,loc):
    end_time = datetime.datetime.utcnow()
    begin_time = end_time-datetime.timedelta(hours=24)
   
    data_count = mongo.db[name].find({"event_time":{"$gte":begin_time}}).count()
    documents = mongo.db[name].find({"event_time":{"$gte":begin_time}})
    t = []
    h = []
    p = []
    for doc in documents:
        if 'temperature' in doc:
            t.append(doc['temperature'])
            h.append(doc['humidity'])
            p.append(doc['pressure'])
    if data_count <= 100:
        slice_amt = 1
    else:
        slice_amt = int(data_count/100) 

    currenttime = datetime.datetime.now().strftime('%A  %-I:%M:%S %p %Z  %b %-d, %Y')
    return render_template('chartnew.html',name=name, location=loc, currenttime=currenttime, 
                    t_data = t[::slice_amt],
                    h_data = h[::slice_amt],
                    p_data = p[::slice_amt]) 


@app.route('/devices')
def list_devices():
    global devices
    devices = []
    device_lst = mongo.db.Device_Name_Mapping.find().sort('_id',pymongo.ASCENDING)
    for i in device_lst:
        devices.append({'col':'device%02d'%int(i['_id']), 'Location':i['Location']})
    return jsonify({'result':devices})


@app.route('/current')
def get_current():
    global devices
    output=[]
    for i in devices:
        data = mongo.db[i['col']].find().sort('$natural',pymongo.DESCENDING).limit(1)
        d = data[0]
        output.append({'Location':i['Location'],
                        'Temperature':d['temperature'],
                        'Pressure':d['pressure'],
                        'Humidity':d['humidity'],
                        'Voltage':d['bat_voltage'],
                        'Event Time':d['event_time'].isoformat()+'Z'})
    return jsonify({'result':output})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
