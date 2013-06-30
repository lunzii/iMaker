# -*- coding:utf-8 -*-
'''
Created on 13-6-29

@author: olunxchen
'''


import serial
from SimpleCV import Camera,HaarCascade
from Arduino import Arduino
import time

PORT = '/dev/tty.usbmodem1a1221'
BAUD = 9600

PIR_INPUT_PIN = 2
TEMP_INPUT_PIN = 3
DIS_TRIG_PIN = 4
DIS_ECHO_PIN = 5
DSM_INPUT_PIN = 0
AIR_INPUT_PIN = 1
LIGHT_INPUT_PIN = 2

def read_sensor(param):
    ser = serial.Serial(PORT, BAUD, timeout=2)
    ser.write(param)
    print("read_motion")
    # time.sleep(1)
    value = None
    while not value:
        value = ser.readline()
        # print 'readline'
    print(value)
    ser.close()
    return value


def read_motion():
    board = Arduino(BAUD, port=PORT)
    print board.digitalRead(PIR_INPUT_PIN)
    cam = Camera()
    haarcascade = HaarCascade("face")
    image = cam.getImage().flipHorizontal().scale(0.5)
    faces = image.findHaarFeatures(haarcascade)
    print faces
    if faces:
        print True
    else:
        print False


def read_temperature():
    result = read_sensor('t').split(',')
    humidity = result[0].split(':')[1]
    temperature = result[1].split(':')[1]
    print humidity
    print temperature
    return humidity,temperature


def read_distance():
    board = Arduino(BAUD, port=PORT)
    # board.pinMode(DIS_TRIG_PIN, "OUTPUT")
    # board.pinMode(DIS_ECHO_PIN, "INPUT")
    #
    # board.digitalWrite(DIS_TRIG_PIN, "LOW")
    # time.sleep(0.000002)
    #
    # board.digitalWrite(DIS_TRIG_PIN, "HIGH")
    # time.sleep(0.000010)
    # board.digitalWrite(DIS_TRIG_PIN, "LOW")

    while True:
        duration = board.pulseIn(DIS_ECHO_PIN, "HIGH")
        print duration
        distance = (duration/2) / 29.1
        print distance
        time.sleep(0.1)


def read_dust():
    board = Arduino(BAUD, port=PORT)
    value = None
    while not value:
        value = board.analogRead(DSM_INPUT_PIN)
    print value


def read_air():
    board = Arduino(BAUD, port=PORT)
    value = None
    while not value:
        value = board.analogRead(AIR_INPUT_PIN)
    print value


def read_light():
    board = Arduino(BAUD, port=PORT)
    value = None
    while not value:
        value = board.analogRead(LIGHT_INPUT_PIN)
    print value


if __name__ == '__main__':
    read_dust()