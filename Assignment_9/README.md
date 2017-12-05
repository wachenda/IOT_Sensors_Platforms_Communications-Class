# NOTES for Assignment 9:

## Overview:

Demonstrate using PubNub to publish and subscribe to data from a BME280 sensor on Raspberry Pi


## Usage:

[![Watch the Assignment 9 Demo Video](https://www.youtube.com/upload_thumbnail?v=z-i04m6NMOg&t=2&ts=1512499066874)](https://youtu.be/z-i04m6NMOg)

## Details

For controlling the RGB LED, we would like to provide a PWM input to each of the 3 LED's in the module.  However, the broadcom MCU on the Raspberry Pi only provides 2 hardware PWM outputs.  One could do bit-banging to simulate a PWM signal but this is very inefficient and will eat up CPU time.

An alternative is to use GPIO DMA to send a PWM signal to any of the GPIO pins.  This avoids use CPU time and is quite effective. Fortunately, someone has written the PiGPIO library in C for the Raspberry Pi that enables this functionallity.  This library can be used in C, C++ or in Python.  Here is the link:  


Controlling the NeoPixel strip is even more tricky than controlling the RGB with PWM signals.  The control signal requires 5-V logic patterns with sub-uSec timing requirements.  In the USER mode of the Raspberry Pi running in Linux, this can be quite a challenge to deliver and would be almost impossible to bit-bang.  In this case, someone has written a C library that takes advantage of either one of the PWM peripherals on the Pi MCU or the SPI peripheral.  Additionally, DMA is used to vary the bit patterns into these peripherals in order to provide their control signals. This library was written by Jeremy Garff and is available at:



