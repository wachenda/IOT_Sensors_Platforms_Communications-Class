# NOTES for Assignment 8:

## Overview:

Create RESTful Service using a BME280 sensor as well as the RGB_LED from Assignment 6

## Example of website:


: ~$curl -i http:/10.0.1.52:8080/api 
HTTP/1.0 200 OK

Content-Type: application/json Content-Length: 204

Server: Werkzeug/0.11.15 Python/3.5.3 Date: Thu, 23 Nov 2017 02:49:35 GMT

{

    "led": {

            "B": 0,

                "G": 0,

                    "R": 0

    }, "sensors": {

        "eventtime": "2017-11-23T02:49:35.333311Z", "humidity": 60.011,

        "pressure": 1009.584,

        "temperature": 70.445

    } }

    : ~$curl -i http:/10.0.1.52:8080/api/sensors HTTP/1.0 200 OK
    Content-Type: application/json Content-Length: 123
    Server: Werkzeug/0.11.15 Python/3.5.3 Date: Thu, 23 Nov 2017 02:49:44 GMT
    {
        "eventtime": "2017-11-23T02:49:44.037690Z", "humidity": 59.972,
        "pressure": 1009.593,
        "temperature": 70.429
    }
    : ~$curl -i http:/10.0.1.52:8080/api/sensors/temperature HTTP/1.0 200 OK
    Content-Type: application/json
    Content-Length: 28
    Server: Werkzeug/0.11.15 Python/3.5.3
    Date: Thu, 23 Nov 2017 02:49:51 GMT
    {
        "temperature": 70.437
    }
    : ~$curl -i http:/10.0.1.52:8080/api/sensors/pressure HTTP/1.0 200 OK
    Content-Type: application/json
    Content-Length: 27
    Server: Werkzeug/0.11.15 Python/3.5.3
     Date: Thu, 23 Nov 2017 02:49:57 GMT
     {
         "pressure": 1009.588
     }
     : ~$curl -i http:/10.0.1.52:8080/api/sensors/humidity HTTP/1.0 200 OK
     Content-Type: application/json
     Content-Length: 24
     Server: Werkzeug/0.11.15 Python/3.5.3
     Date: Thu, 23 Nov 2017 02:50:04 GMT
     {
         "humidity": 60.01
     }
     : ~$curl -i http:/10.0.1.52:8080/api/led HTTP/1.0 200 OK
     Content-Type: application/json Content-Length: 35
     Server: Werkzeug/0.11.15 Python/3.5.3 Date: Thu, 23 Nov 2017 02:50:11 GMT
     {
         "B": 0,
         "G": 0,
         "R": 0 }
         : ~$curl -i -H "Content-type: application/json" -X POST -d "{\"R\":255,\"G\":0,\"B\":0}" http://10.0.1.52:8080/api/led HTTP/1.0 200 OK
         Content-Type: application/json
         Content-Length: 37
         Server: Werkzeug/0.11.15 Python/3.5.3 Date: Thu, 23 Nov 2017 02:50:32 GMT
         {
             "B": 0,
             "G": 0,
             "R": 255 }
             : ~$curl -i -H "Content-type: application/json" -X POST -d "{\"R\":0,\"G\":255,\"B\":0}" http://10.0.1.52:8080/api/led HTTP/1.0 200 OK
             Content-Type: application/json
             Content-Length: 37
             Server: Werkzeug/0.11.15 Python/3.5.3 Date: Thu, 23 Nov 2017 02:50:49 GMT
             {
                 "B": 0,
                 "G": 255,
                 "R": 0 }
                 : ~$curl -i -H "Content-type: application/json" -X POST -d "{\"R\":0,\"G\":0,\"B\":255}" http://10.0.1.52:8080/api/led HTTP/1.0 200 OK
                 Content-Type: application/json
                 Content-Length: 37
                 Server: Werkzeug/0.11.15 Python/3.5.3 Date: Thu, 23 Nov 2017 02:51:02 GMT
                 {
                       "B": 255,
                         "G": 0,
                           "R": 0
                 }
                 : ~$curl -i -H "Content-type: application/json" -X POST -d "{\"R\":0,\"G\":0,\"B\":255}" http://10.0.1.52:8080/api/led



![](Images/IMG_2151.jpg?raw=true)

![](Images/IMG_2148.jpg?raw=true)

![](Images/IMG_2149.jpg?raw=true)

![](Images/IMG_2150.jpg?raw=true)


![Model View Controller](RESTful Demo.pdf)
