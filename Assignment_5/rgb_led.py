#!/usr/bin/python3

import argparse
import pigpio

# Raspberry Pi GPIO pins to connect to
R = 4
G = 17
B = 22


parser = argparse.ArgumentParser()
parser.add_argument("Red", help="Red Value:  0 <= value <= 255",
                    type=int)
parser.add_argument("Green", help="Green Value:  0 <= value <= 255",
                    type=int)
parser.add_argument("Blue", help="Blue Value:  0 <= value <= 255",
                    type=int)
args = parser.parse_args()

# print(args)

# print(args.Red)
# print(args.Green)
# print(args.Blue)

p = pigpio.pi()


p.set_PWM_frequency(R,8000)
#print(p.set_PWM_frequency(G,8000))
#print(p.set_PWM_frequency(B,8000))


p.set_PWM_dutycycle(R,args.Red)
p.set_PWM_dutycycle(G,args.Green)
p.set_PWM_dutycycle(B,args.Blue)
