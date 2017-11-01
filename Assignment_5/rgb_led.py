#!/usr/bin/python3

import argparse
import pigpio

# Raspberry Pi GPIO pins to connect to
R = 4	# GPIO04
G = 17	# GPIO17
B = 22	# GPIO22

def range_type(x):
    x = int(x)
    if x < 0 or x > 255:
        raise argparse.ArgumentTypeError("Value must >= 0 and <= 255")
    return x

# Parse command line arguments
parser = argparse.ArgumentParser(description='Applicaton to set color of RGB LED on Raspberry Pi')
parser.add_argument("Red", type=range_type, help="Red Value:  0 <= value <= 255")
parser.add_argument("Green",type=range_type, help="Green Value:  0 <= value <= 255")
parser.add_argument("Blue", type=range_type, help="Blue Value:  0 <= value <= 255")
args = parser.parse_args()


if __name__ == '__main__':

	# Initialize pigpio
	p = pigpio.pi()
	
	# Set PWM frequency (only need to set for one GPIO and other GPIO's will use the same frequency) 
	p.set_PWM_frequency(R,8000)
	#print(p.set_PWM_frequency(G,8000))
	#print(p.set_PWM_frequency(B,8000))

	# Set RGB color for LED based on command line input
	p.set_PWM_dutycycle(R,args.Red)
	p.set_PWM_dutycycle(G,args.Green)
	p.set_PWM_dutycycle(B,args.Blue)
