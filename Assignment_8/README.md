# NOTES for Assignment 8:

## Overview:

Create RESTful Service using a BME280 sensor as well as the RGB_LED from Assignment 6

## Demonstration of RESTful API:

## ~ $ curl -i http:/10.0.1.52:8080/api 

HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 203
Server: Werkzeug/0.11.15 Python/3.5.3
Date: Tue, 28 Nov 2017 17:16:04 GMT

{
      "led": {
          "B": 0, 
          "G": 0, 
          "R": 0
       }, 
       "sensors": {
          "eventtime": "2017-11-28T17:16:04.404934Z", 
          "humidity": 52.88, 
          "pressure": 1011.674, 
          "temperature": 66.073
       }
}


## ~ $ curl -i http:/10.0.1.52:8080/api/sensors

HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 123
Server: Werkzeug/0.11.15 Python/3.5.3
Date: Tue, 28 Nov 2017 17:17:51 GMT

{
      "eventtime": "2017-11-28T17:17:51.293908Z", 
      "humidity": 53.266, 
      "pressure": 1011.691, 
      "temperature": 66.033
}

## ~ $ curl -i http:/10.0.1.52:8080/api/sensors/temperature

HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 28
Server: Werkzeug/0.11.15 Python/3.5.3
Date: Tue, 28 Nov 2017 17:22:44 GMT

{
      "temperature": 66.094
}

## ~ $ curl -i http:/10.0.1.52:8080/api/sensors/pressure

HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 26
Server: Werkzeug/0.11.15 Python/3.5.3
Date: Tue, 28 Nov 2017 17:23:28 GMT

{
      "pressure": 1011.72
}

## ~ $ curl -i http:/10.0.1.52:8080/api/sensors/humidity 

HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 25
Server: Werkzeug/0.11.15 Python/3.5.3
Date: Tue, 28 Nov 2017 17:24:12 GMT

{
      "humidity": 54.087
}

## ~ $ curl -i http:/10.0.1.52:8080/api/led

HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 35
Server: Werkzeug/0.11.15 Python/3.5.3
Date: Tue, 28 Nov 2017 17:24:50 GMT

{
      "B": 0, 
        "G": 0, 
          "R": 0
}

![](Images/IMG_2151.jpg?raw=true)



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
