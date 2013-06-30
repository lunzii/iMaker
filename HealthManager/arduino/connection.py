# # -*- coding:utf-8 -*-
# '''
# Created on 13-6-29
#
# @author: olunxchen
# '''
#
#
# import serial
# from SimpleCV import Camera,HaarCascade
#
# PORT = '/dev/tty.usbmodem1431'
# BAUD = 9600
#
#
# def read_sensor(param):
#     ser = serial.Serial(PORT, BAUD, timeout=2)
#     ser.write(param)
#     print("read_motion")
#     # time.sleep(1)
#     value = None
#     while not value:
#         value = ser.readline()
#         # print 'readline'
#     print(value)
#     ser.close()
#     return value
#
#
# def read_motion():
#     sensor = read_sensor('m')
#     sensor = bool(sensor.split(':')[1])
#     print sensor
#     cam = Camera()
#     haarcascade = HaarCascade("face")
#     image = cam.getImage().flipHorizontal().scale(0.5)
#     faces = image.findHaarFeatures(haarcascade)
#     print faces
#     if faces or sensor:
#         print True
#     else:
#         print False
#
#
# def read_temperature():
#     result = read_sensor('t').split(',')
#     humidity = result[0].split(':')[1]
#     temperature = result[1].split(':')[1]
#     print humidity
#     print temperature
#     return humidity,temperature
#
#
# def read_distance():
#     distance = read_sensor('d').split(':')[1]
#     print distance
#     if int(distance) < 10:
#         return True
#     else:
#         return False
#
#
# def read_dust():
#     dust = read_sensor('f').split(':')[1]
#     print dust
#     return dust
#
#
# def read_air():
#     air = read_sensor('a').split(':')[1]
#     print air
#     return air
#
#
# def read_light():
#     light = read_sensor('l').split(':')[1]
#     print light
#     return light
#
#
# if __name__ == '__main__':
#     read_distance()