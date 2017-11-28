#!/usr/bin/python3

from flask import Flask, render_template, request, jsonify
import datetime
import atexit

from bme280 import *
from rgb_led import *

sensor = BME280(t_mode=BME280_OSAMPLE_8, p_mode=BME280_OSAMPLE_8, h_mode=BME280_OSAMPLE_8)
BUS = 1
BME280_I2C_ADDR=0x77

rgb = RGB()
rgb.set_RGB(255,0,0)


app = Flask(__name__)

api = { 'sensors' : 
        {
            'temperature' : 20., 
            'humidity' : 50.,
            'pressure' : 1000.,
            'eventtime' :''
        },
        'led':
        {
            'R' : 0,
            'G' : 0,
            'B' : 0
        }
    }

def current_time():
	utc_datetime = datetime.datetime.utcnow()
	datestr = utc_datetime.isoformat()
	return datestr+'Z'
 

def get_BME280_measurement():
    # sensors = [i['sensors'] for i in api if 'sensors' in i]
    api['sensors']['temperature'] = round(sensor.read_temperature_f(),3)
    api['sensors']['pressure'] = round(sensor.read_pressure(),3)
    api['sensors']['humidity'] = round(sensor.read_humidity(),3)
    api['sensors']['eventtime'] = current_time()

@app.route('/')
def index():
	return 'Assignment 8 - A RESTful Service'

@app.route('/api', methods =['GET'])
def returnAll():
    get_BME280_measurement()
    return jsonify(api)

@app.route('/api/sensors', methods =['GET'])
def returnSensorsAll():
    get_BME280_measurement()
    return jsonify(api['sensors'])

@app.route('/api/sensors/temperature', methods =['GET'])
def returnSensorsTemperature():
    get_BME280_measurement()
    return jsonify({'temperature':api['sensors']['temperature']})

@app.route('/api/sensors/humidity', methods =['GET'])
def returnSensorsHumidity():
    get_BME280_measurement()
    return jsonify({'humidity': api['sensors']['humidity']})

@app.route('/api/sensors/pressure', methods =['GET'])
def returnSensorsPressure():
    get_BME280_measurement()
    return jsonify({'pressure': api['sensors']['pressure']})

@app.route('/api/led', methods =['GET'])
def returnLED_RGB():
    return jsonify(api['led'])

@app.route('/api/led', methods =['POST'])
def setLED_RGB():
    #data = request.get_json()
    #print(data)
    #api['led']['R'] = data['R']
    #api['led']['G'] = data['G']
    #api['led']['B'] = data['B']
    api['led']['R'] = request.json['R']
    api['led']['G'] = request.json['G']
    api['led']['B'] = request.json['B']
    rgb.set_RGB(api['led']['R'],api['led']['G'],api['led']['B'])
    return jsonify(api['led'])
    
@atexit.register
def cleanup():
    print()
    print('Cleaning up and exiting')

if __name__ == '__main__':
    get_BME280_measurement()
    app.run(debug=False, host='0.0.0.0', port=8080)
