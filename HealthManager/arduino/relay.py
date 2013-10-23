# -*- coding:utf-8 -*-
'''
Created on 13-8-11

@author: olunxchen
'''


import RPi.GPIO as GPIO
import time

# GPIO.setmode(GPIO.BCM)

RELAY_1 = 24
RELAY_2 = 25

print 'Relay Control'


class Relay:
    pin = 0

    def __init__(self, relay_pin):
        self.pin = relay_pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)
        GPIO.output(self.pin, GPIO.LOW)

    def turn_on(self):
        GPIO.output(self.pin, GPIO.HIGH)

    def turn_off(self):
        GPIO.output(self.pin, GPIO.LOW)

if __name__ == "__main__":
    lamp = Relay(RELAY_1)
    while 1:
        lamp.turn_on()
        time.sleep(10)
        lamp.turn_off()
        time.sleep(10)