#!/usr/bin/python3

import pigpio
import atexit

GPIO4 = 4   # GPIO04
GPIO17 = 17  # GPIO17
GPIO22 = 22  # GPIO22

class RGB(object):
    def __init__(self, R=GPIO4, G=GPIO17, B=GPIO22):
        self._R = R
        self._G = G
        self._B = B
        
        self._pi = pigpio.pi()

        # Set PWM frequency (only need to set for one GPIO and other GPIO's will use the same frequency)
        self._pi.set_PWM_frequency(self._R,8000)

        # Initialize all colors to OFF
        self._RED = 0
        self._GREEN = 0
        self._BLUE = 0

        # Set RGB color for LED 
        self._pi.set_PWM_dutycycle(self._R,self._RED)
        self._pi.set_PWM_dutycycle(self._G,self._GREEN)
        self._pi.set_PWM_dutycycle(self._B,self._BLUE)

        atexit.register(self.cleanup)

    def cleanup(self):
        self._pi.stop()

    def set_RGB(self, Red=0, Green=0, Blue=0):
        self._RED = Red
        self._GREEN = Green
        self._BLUE = Blue

        # Set RGB color for LED
        self._pi.set_PWM_dutycycle(self._R,self._RED)
        self._pi.set_PWM_dutycycle(self._G,self._GREEN)
        self._pi.set_PWM_dutycycle(self._B,self._BLUE)

