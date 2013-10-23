__author__ = 'sdx'
# -*- coding:utf-8 -*-
import os
import time
import Image as image
import views
import commands
#定义反过斜杠，方便适配linux
slash = "/"
deviceFileDir = "/sdcard/DCIM/100MEDIA/"
#定义iPhone的图片路径
deviceFileDirIphone = "/home/pi/.gvfs/iPhone/DCIM/100APPLE/"
dateTimeList = []
getFileCount = 0
addIphonePath = "/HealthManager/HealthManager/res"


def getFileList(fileType, inputTime):
    """
    The input para is the file be save last time. Important!!!
    """
    global getFileCount
    print "Get fileList which type is:" + fileType
    fileList = [];
    #str = os.popen("adb shell ls -l /sdcard/DCIM/100MEDIA/").read()
    str = os.popen("adb shell ls -l " + deviceFileDir).read()
    listArray = str.split("\n")
    for list in listArray:
        items = list.split(" ")
        i = 0
        length = len(items)
        if length >= 3:
            date = items[length - 3]
            #print date
            time = items[length - 2]
            #print time
            filename = items[length - 1]
            #print filename
            #统一成没有空格的形式2013-08-0809:30
            dateTime = date + time
            #print "dateTime is:" + dateTime
            #print "inputTime is:" + inputTime
            #file must be new
            if(dateTime > inputTime):
                #insert name to the picList
                if filename.find(fileType) != -1:
                    if getFileCount == 0:
                        dateTimeList.append(dateTime)
                    filename = filename[0: len(filename) - 1]
                    fileList.append(filename)
    getFileCount = 1
    return  fileList

'''
sourceLocation是默认指"/sdcard/DCIM/100MEDIA/"
destLocation此处利用设备号作为一级目录
fileList都是.jpg文件的名字
'''
def copyFile(fileList, sourceLocation, destLocation):
    print "Copy file from the device:" + getSystemTime()
    for fileName in fileList:
        #print "Copy " + fileName + " to " + destLocation
        copyCmd = "adb pull " + sourceLocation + fileName + " " + "home/pi/helper_img/" + destLocation + "/" + fileName;
        #print copyCmd
        print copyCmd
        os.popen(copyCmd)

    print "Copy file form devices finish!" + getSystemTime()

def getDeviceId():
    #strDeviceId = commands.getstatusoutput("adb shell dumpsys iphonesubinfo")

    strDeviceId = os.popen("adb shell dumpsys iphonesubinfo").read()
    lengthPos = len(strDeviceId)
    #print lengthPos
    idPos = strDeviceId.find("ID")
    #print idPos,E:\testCopy\355868051021567\r
    deviceId = strDeviceId[idPos + 5: lengthPos - 2]
    return deviceId

def createDir(dirPath):
    """
    create the dir if not exist
    :param deviceId:
    """

    #recognize if the file is exist

    #print "---------------come in createDir------------------" + dirPath
    if not os.path.exists(dirPath):
        #print "---------------Real come in createDir------------------"
        print "create Dir", dirPath
        #os.mkdir(dirPath)
        os.system("mkdir " + dirPath)
    else:
        print dirPath, "is always exist"

def getSystemTime():
    return time.strftime('%Y-%m-%d %H:%M')

#input:fileList，要压缩的路径
def picCompress(fileList, allDirPath):
    print "File compression"
    #目标图片大小
    dst_w = 250
    dst_h = 250
    #保存的图片质量
    save_q = 45
    for fileName in fileList:
        #图片路径
        allFilePath = allDirPath + slash + fileName
        pos = allFilePath.find(".");
        smallPicPath =allFilePath[0: pos] + "_s" + allFilePath[pos: len(allFilePath)]
        ori_img = allFilePath
        #目标图片
        dst_img = smallPicPath
        #等比例压缩图片
        resizeImg(ori_img=ori_img,dst_img=dst_img,dst_w=dst_w,dst_h=dst_h,save_q=save_q)

    print "File compress finished!"


#等比例压缩图片
def resizeImg(**args):
    args_key = {'ori_img':'','dst_img':'','dst_w':'','dst_h':'','save_q':75}
    arg = {}
    for key in args_key:
        if key in args:
            arg[key] = args[key]

    im = image.open(arg['ori_img'])
    ori_w,ori_h = im.size
    widthRatio = heightRatio = None
    ratio = 1
    if (ori_w and ori_w > arg['dst_w']) or (ori_h and ori_h > arg['dst_h']):
        if arg['dst_w'] and ori_w > arg['dst_w']:
            widthRatio = float(arg['dst_w']) / ori_w #正确获取小数的方式
        if arg['dst_h'] and ori_h > arg['dst_h']:
            heightRatio = float(arg['dst_h']) / ori_h

        if widthRatio and heightRatio:
            if widthRatio < heightRatio:
                ratio = widthRatio
            else:
                ratio = heightRatio

        if widthRatio and not heightRatio:
            ratio = widthRatio
        if heightRatio and not widthRatio:
            ratio = heightRatio

        newWidth = int(ori_w * ratio)
        newHeight = int(ori_h * ratio)
    else:
        newWidth = ori_w
        newHeight = ori_h

    im.resize((newWidth,newHeight),image.ANTIALIAS).save(arg['dst_img'],quality=arg['save_q'])


def classfyPic(picList, dateTimeList, allDirPath):
    print "Begin classify Pictures:" + getSystemTime()
    for i in range(0, picList.__len__()):
        copyCmd = "cp " + allDirPath + slash + picList[i] + " " + allDirPath + slash + dateTimeList[i][0: 10] + slash + dateTimeList[i][0:12] + picList[i];
        #allDirPath = os.getcwd() + "_img" + slash + getDeviceId()
        print copyCmd;
        pos = picList[i].find(".");
        newPicList = picList[i][0: pos] + "_s"  + picList[i][pos: len(picList[i])]
        copySmallCmd = "cp " + allDirPath + slash + newPicList + " " + allDirPath + slash + dateTimeList[i][0: 10] + slash + dateTimeList[i][0:12] + newPicList;
        print copySmallCmd
        delPicCmd = "rm " + allDirPath + slash + picList[i]
        delSmallCmd = "rm " + allDirPath + slash + newPicList

        #print copyCmd
        #print copySmallCmd
        os.system(copyCmd)
        os.system(copySmallCmd)
        #复制完后删除文件
        os.system(delPicCmd)
        os.system(delSmallCmd)
        #封装字典后插入数据库
        dic = {}

        #设备id
        dic["device_folder_id"] = getDeviceId()

        #文件名
        dic["device_folder_name"] = getDeviceId()

        #子文件ID
        dic["type_folder_id"] = dateTimeList[i][0: 10]

        #子文件夹名
        dic["type_folder_name"] = dateTimeList[i][0: 10]

        #小图片名称
        dic["small_name"] = newPicList

        #图片名称
        dic["name"] = picList[i]

        #本地路径
        dic["path"] = os.getcwd() + "_img"

        #时间
        dic["date_time"] = dateTimeList[i]

        #在此插入数据库
        views.insert_data_photo(dic)


        lastTimeStr = time.strftime('%Y-%m-%d%H:%M')
        #global lastTime
        #lastTime = "2013-08-1100:57"



        # dic = {}
        # dic["device_id"] = getIphoneDeviceId()
        # dic["date"] = lastTimeStr
        #
        # #在此插入数据库
        # views.insert_data_device(dic)


        print("Insert to database finished!")


def classfyPicIphone(picList, dateTimeList, allDirPath):
    print "Begin classify Pictures:" + getSystemTime()
    for i in range(0, picList.__len__()):
        copyCmd = "cp -i " + allDirPath + slash + picList[i] + " " + allDirPath + slash + dateTimeList[i][0: 10] + slash + dateTimeList[i][0:12] + picList[i];
        pos = picList[i].find(".");
        newPicList = picList[i][0: pos] + "_s"  + picList[i][pos: len(picList[i])]
        copySmallCmd = "cp -i " + allDirPath + slash + newPicList + " " + allDirPath + slash + dateTimeList[i][0: 10] + slash + dateTimeList[i][0:12] + newPicList;

        delPicCmd = "rm " + allDirPath + slash + picList[i]
        delSmallCmd = "rm " + allDirPath + slash + newPicList

        #print copyCmd
        #print copySmallCmd
        os.system(copyCmd)
        os.system(copySmallCmd)
        #复制完后删除文件
        os.system(delPicCmd)
        os.system(delSmallCmd)
        #封装字典后插入数据库
        dic = {}

        #设备id
        dic["device_folder_id"] = getDeviceId()

        #文件名
        dic["device_folder_name"] = getDeviceId()

        #子文件ID
        dic["type_folder_id"] = dateTimeList[i][0: dateTimeList.__len__]

        #子文件夹名
        dic["type_folder_name"] = dateTimeList[i][0: dateTimeList.__len__]

        #小图片名称
        dic["small_name"] = newPicList

        #图片名称
        dic["name"] = picList[i]

        #本地路径
        dic["path"] = os.getcwd() + "_img"

        #时间
        dic["date_time"] = dateTimeList[i]

        #在此插入数据库
        views.insert_data_photo(dic)
        print("Insert to database finished!")

        lastTimeStr = time.strftime('%d%H:%M')
        #global lastTime
        #lastTime = "2013-08-1100:57"

        dic = {}
        dic["device_id"] = getDeviceId()
        dic["date"] = lastTimeStr

        #在此插入数据库
        views.insert_data_device(dic)




    print "Classify Pictures Finish!" + getSystemTime()

def creatClassifyFolder(dataTimeList, allDirPath):
    print "Begin create classfy Dir!"
    for c in dateTimeList:
        classifyDir = allDirPath + slash + c[0: 10]
        createDir(classifyDir)
    print "Classfy Dir create finish!"


#适配Iphone
def getIphoneDeviceId():
    strDeviceId = os.popen("idevicepair validate").read()
    lengthPos = len(strDeviceId)
    #print lengthPos
    idPos = strDeviceId.find("device")
    #print idPos,E:\testCopy\355868051021567\r
    deviceId = strDeviceId[idPos + 7: lengthPos - 2]
    return deviceId

def doFile1():
    print "hello doFile1"
#整个流程
def doFile():

    print getDeviceId()
    print os.getcwd() + "_img"
    #E:\testCopy\355868051021567
    allDirPath = os.getcwd() + "_img" + slash + getDeviceId()
    #如果没有存在，表示该设备第一次插入
    print allDirPath
    if not os.path.exists(allDirPath):
	
        #建设备文件夹
        #os.mkdir(allDirPath)
        os.popen("mkdir " + allDirPath)

        #复制全部文件，同时初始化dataTimeList:2013-08-1010:38
        #设置为2010，拷贝整个文件夹
        initTime = "0"

        #获取所有图片的列表
        picList = getFileList(".jpg", initTime)

        #从android拷贝所有文件文件
        copyFile(picList, deviceFileDir, getDeviceId())

        #图片压缩
        picCompress(picList, allDirPath)

        #建图片分类文件夹
        creatClassifyFolder(dateTimeList, allDirPath)

        #图片分类
        classfyPic(picList, dateTimeList, allDirPath)

        #在此插入数据库（切记插入当前的时间戳）

        # lastTimeStr = time.strftime('%Y-%m-%d%H:%M')
        # #global lastTime
        # #lastTime = "2013-08-1100:57"
        #
        # dic = {}
        # dic["device_id"] = lastTimeStr
        #
        # #在此插入数据库
        # views.insert_data_device(dic)
    
    
    #表示该设备之前插入过
    else:
        #global lastTime

        #从数据库获取lastTime的值
        #lastTime = views.get_date_by_deviceid(getDeviceId())

        lastTime = "2013-08-1100:00";
        print getDeviceId() + "is always exist"
        #获取所有图片的列表
        picList = getFileList(".jpg", lastTime)

        #从android拷贝所有文件文件
        copyFile(picList, deviceFileDir, getDeviceId())

        #图片压缩
        picCompress(picList, allDirPath)

        #建图片分类文件夹
        creatClassifyFolder(dateTimeList, allDirPath)

        #图片分类
        classfyPic(picList, dateTimeList, allDirPath)

        # lastTimeStr = time.strftime('%Y-%m-%d%H:%M')
        # #global lastTime
        # #lastTime = "2013-08-1100:57"
        # dic = {}
        # dic["device_id"] = lastTimeStr
        #
        # #在此插入数据库
        # #views.insert_data_device(dic)




def getIphoneFileList(fileType, inputTime):
    """
    The input para is the file be save last time. Important!!!
    """
    global getFileCount
    print "Get fileList which type is:" + fileType
    fileList = [];
    #str = os.popen("adb shell ls -l /sdcard/DCIM/100MEDIA/").read()
    str = os.popen("ls -l " + deviceFileDirIphone).read()
    listArray = str.split("\n")
    for list in listArray:
        items = list.split(" ")
        i = 0
        length = len(items)
        if length >= 3:
            date = items[length - 3]
            #print date
            time = items[length - 2]
            #print time
            filename = items[length - 1]
            #print filename
            #统一成没有空格的形式2013-08-0809:30
            dateTime = date + time
            #print "dateTime is:" + dateTime
            #print "inputTime is:" + inputTime
            #file must be new
            if(dateTime > inputTime):
                #insert name to the picList
                if filename.find(fileType) != -1:
                    if getFileCount == 0:
                        dateTimeList.append(dateTime)
                    filename = filename[0: len(filename) - 1]
                    fileList.append(filename)
    getFileCount = 1
    return  fileList


def creatClassifyFolderIphone(dataTimeList, allDirPath):
    print "Begin create classfy Dir!"
    for c in dateTimeList:
        classifyDir = allDirPath + slash + c[0: dateTimeList.__len__()]
        createDir(classifyDir)
    print "Classfy Dir create finish!"


def copyFileIphone(fileList, sourceLocation, destLocation):
    print "Copy file from the device:" + getSystemTime()
    for fileName in fileList:
        #print "Copy " + fileName + " to " + destLocation
        copyCmd = "cp " + sourceLocation + fileName + " " + "./" + destLocation + "/" + fileName;
        #print copyCmd
        os.popen(copyCmd)

    print "Copy file form devices finish!" + getSystemTime()

def setIphonePath():
    print "Setting iphone path..."


def doFileIphone():
    print "iphone"
    print getIphoneDeviceId()
    print os.getcwd() + "_img"
    #E:\testCopy\355868051021567
    allDirPath = os.getcwd() + "_img" + slash + getIphoneDeviceId()
    #如果没有存在，表示该设备第一次插入
    print allDirPath
    if not os.path.exists(allDirPath):
        #建设备文件夹
        os.mkdir(allDirPath)

        #复制全部文件，同时初始化dataTimeList:2013-08-1010:38
        #设置为2010，拷贝整个文件夹
        initTime = "2000"

        #获取所有图片的列表
        picList = getIphoneFileList(".jpg", initTime)

        #从Iphone拷贝所有文件文件
        copyFileIphone(picList, deviceFileDirIphone, getIphoneDeviceId())

        #图片压缩
        picCompress(picList, allDirPath)

        #建图片分类文件夹
        creatClassifyFolderIphone(dateTimeList, allDirPath)

        #图片分类
        classfyPicIphone(picList, dateTimeList, allDirPath)

        #在此插入数据库（切记插入当前的时间戳）

        # lastTimeStr = time.strftime('%d%H:%M')
        # #global lastTime
        # #lastTime = "2013-08-1100:57"
        #
        #
        # dic = {}
        # dic["device_id"] = lastTimeStr
        #
        # #在此插入数据库
        # views.insert_data_device(dic)


    #表示该设备之前插入过
    else:
        #global lastTime

        #从数据库获取lastTime的值
        lastTime = views.get_date_by_deviceid(getDeviceId())

        print getDeviceId() + "is always exist"

        #获取所有图片的列表
        picList = getIphoneFileList(".jpg", initTime)

        #从Iphone拷贝所有文件文件
        copyFileIphone(picList, deviceFileDirIphone, getIphoneDeviceId())

        #图片压缩
        picCompress(picList, allDirPath)

        #建图片分类文件夹
        creatClassifyFolderIphone(dateTimeList, allDirPath)

        #图片分类
        classfyPicIphone(picList, dateTimeList, allDirPath)

        #在此插入数据库（切记插入当前的时间戳）

        # lastTimeStr = time.strftime('%d%H:%M')
        # #global lastTime
        # #lastTime = "2013-08-1100:57"
        #
        # dic = {}
        # dic["device_id"] = lastTimeStr
        #
        # #在此插入数据库
        # views.insert_data_device(dic)

        # #获取所有图片的列表
        # picList = getFileList(".jpg", lastTime)
        #
        # #从android拷贝所有文件文件
        # copyFile(picList, deviceFileDir, getDeviceId())
        #
        # #图片压缩
        # picCompress(picList, allDirPath)
        #
        # #建图片分类文件夹
        # creatClassifyFolder(dateTimeList, allDirPath)
        #
        # #图片分类
        # classfyPic(picList, dateTimeList, allDirPath)
        #
        # lastTimeStr = time.strftime('%Y-%m-%d%H:%M')
        # #global lastTime
        # #lastTime = "2013-08-1100:57"
        # dic = {}
        # dic["device_id"] = lastTimeStr

        #在此插入数据库
        #views.insert_data_device(dic)



