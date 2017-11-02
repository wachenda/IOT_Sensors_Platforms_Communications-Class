# NOTES for Assignment 5:

## Overview:

Write a program to control LED an LED through a GPIO on the Pi.


For this assignment, I decided to "amp" it up and demonstrate controlling an RGB LED using GPIO DMA hardware generated PWM signals.  The program to do this is **rgb_led.py**

Also, I wrote a program to control a strip of NeoPixel (WS2812) LED's.  The program to do this is **rgb_neo.py**

The current capabilities of the GPIO pins on the Pi are not very high. Therefore, I utilized N-channel MOSFETS to interface to the RGB LED as well as the NeoPixel.  The schematics for wiring these configurations is shown below.

## Usage:

**$ ./rgb_led.py**
usage: rgb_led.py [-h] Red Green Blue


**$ sudo ./rgb_neo.py**
usage: rgb_neo.py [-h] Red Green Blue

## Details

For controlling the RGB LED, we would like to provide a PWM input to each of the 3 LED's in the module.  However, the broadcom MCU on the Raspberry Pi only provides 2 hardware PWM outputs.  One could do bit-banging to simulate a PWM signal but this is very inefficient and will eat up CPU time.

An alternative is to use GPIO DMA to send a PWM signal to any of the GPIO pins.  This avoids use CPU time and is quite effective. Fortunately, someone has written the PiGPIO library in C for the Raspberry Pi that enables this functionallity.  This library can be used in C, C++ or in Python.  Here is the link:  

[Python Interface for pigpio library](http://abyz.me.uk/rpi/pigpio/python.html)

Controlling the NeoPixel strip is even more tricky than controlling the RGB with PWM signals.  The control signal requires 5-V logic patterns with sub-uSec timing requirements.  In the USER mode of the Raspberry Pi running in Linux, this can be quite a challenge to deliver and would be almost impossible to bit-bang.  In this case, someone has written a C library that takes advantage of either one of the PWM peripherals on the Pi MCU or the SPI peripheral.  Additionally, DMA is used to vary the bit patterns into these peripherals in order to provide their control signals. This library was written by Jeremy Garff and is available at:

[rpi_ws281x libary](https://github.com/jgarff/rpi_ws281x)


## Raspberry Pi with RGB LED Schematic:

![](Images/RGB-LED-Schematic.png?raw=true)

## Raspberry Pi with NeoPixel LED Schematic:

![](Images/NeoPixel-LED-Schematic.png?raw=true)
