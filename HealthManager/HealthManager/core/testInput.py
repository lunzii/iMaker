__author__ = 'sdx'
# -*- coding:utf-8 -*-
import time
import os
import copy
def isAndroidInput():
    #print "Test if android is input?"
    strDeviceId = os.popen("adb devices").read()
    #print strDeviceId

    listArray = strDeviceId.split("\n")
    '''for list in listArray:
        print list
    #print listArray.__len__()
    '''
    if listArray.__len__() <= 3:
        return False
    else:
        return True
    '''
    if strDeviceId.find("device") == -1:
        #print "Android device " + getDeviceId() + " is input"
        return True
    else:
        return False
    '''

def isIphoneInput():
    #print "Test if Iphone is input?"
    strDeviceId = os.popen("idevicepair validate").read();
    #print strDeviceId
    if strDeviceId.find("SUCCESS") != -1:
        #print "Iphone device " + getIphoneDeviceId() + " is input"
        return True
    else:
        return False


def getDeviceId():
    strDeviceId = os.popen("adb shell dumpsys iphonesubinfo").read()
    lengthPos = len(strDeviceId)
    #print lengthPos
    idPos = strDeviceId.find("ID")
    #print idPos,E:\testCopy\355868051021567\r
    deviceId = strDeviceId[idPos + 5: lengthPos - 2]
    return deviceId

def getIphoneDeviceId():
    strDeviceId = os.popen("idevicepair validate").read()
    lengthPos = len(strDeviceId)
    #print lengthPos
    idPos = strDeviceId.find("device")
    #print idPos,E:\testCopy\355868051021567\r
    deviceId = strDeviceId[idPos + 7: lengthPos - 2]
    return deviceId

androidDevice = ""
iphoneDevice = ""

def testDeviceInput():
    print "Test if device is input..."
    #while(True):
    #time.sleep(1)
    global androidDevice
    global iphoneDevice
    if isAndroidInput() and (getDeviceId() != androidDevice):
        androidDevice = getDeviceId()
        dic = {}
        dic["device_name"] = androidDevice
        #在此插入数据库
        print "Android is input!"
        copy.doFile()
        androidDevice = ""
    #time.sleep(1)
    if isIphoneInput() and (getIphoneDeviceId() != iphoneDevice) :
        print "Iphone is input!"
        iphoneDevice = getIphoneDeviceId()
        dic = {}
        dic["device_name"] = iphoneDevice
        #copy.doFileIphone()
        iphoneDevice = ""

#testDeviceInput()



