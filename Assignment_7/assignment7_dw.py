#!/usr/bin/python3
# Assignment 7
# David Wachenschwanz
# Example using a Adafruit i2c LCD Pi Plate
import Adafruit_CharLCD as LCD


# Initialize the LCD using the pins
lcd = LCD.Adafruit_CharLCDPlate()


lcd.set_color(1.0, 0.0, 0.0)
lcd.clear()
lcd.message('     David\n Wachenschwanz')