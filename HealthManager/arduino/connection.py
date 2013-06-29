# -*- coding:utf-8 -*-
'''
Created on 13-6-29

@author: olunxchen
'''


import serial
import time

PORT = '/dev/tty.usbmodem1431'
BAUD = 9600


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
    return read_sensor('m')


def read_temperature():
    return read_sensor('t')


def read_distance():
    return read_sensor('d')


def read_dust():
    return read_sensor('f')


def read_air():
    return read_sensor('a')


def read_light():
    return read_sensor('l')


if __name__ == '__main__':
    read_light()