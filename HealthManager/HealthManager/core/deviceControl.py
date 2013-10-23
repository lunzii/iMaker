__author__ = 'sdx'
import os

def getAndroidPower():
    getPowerCmd = "adb shell cat /sys/class/power_supply/battery/capacity"
    str = os.popen(getPowerCmd).read()
    listArray = str.split("\n")
    return listArray[0]

def getIphonePower():
    getPowerCmd = "ideviceinfo -q com.apple.mobile.battery"
    str = os.popen(getPowerCmd).read()
    listArray = str.split("\n")
    if listArray[0].__len__() > 0:
        pos = listArray[0].find(":")
        listArray[0] =listArray[0][pos + 1: len(listArray[0])]
    if listArray[0].find("No device") != -1:
        return ""
    else:
        return listArray[0]

def startGame():
    startGameCmd = "/home/pi/emulators/fba/fba2x /home/pi/emulators/fba/roms/dino.zip"
    os.popen(startGameCmd)

def stopGame():
    stopGameCmd = "kill -9 $(pidof fba2x)"
    os.popen(stopGameCmd)

#demo
print getAndroidPower()
#print getIphonePower()
#startGame()
#stopGame()

