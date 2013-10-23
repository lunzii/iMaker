# -*- coding:utf-8 -*-
'''
Created on 13-6-29

@author:
'''
import json
import threading
from arduino import relay
import copy
import deviceControl
from django.core.serializers import serialize
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils import simplejson
from HealthManager.core.models import ManagerVideo, ManagerPhoto, ManagerStatus, ManagerDevice

def index(request):
    try:
        update_page_status('idle')
    except:
        pass

    return render_to_response('index.html')

def m(request):
    template ='mobile.html'

    objs_device = ManagerPhoto.objects.all().values('device_folder_id').distinct()

    re_list = []
    for device in objs_device:
        device_id = device['device_folder_id']
        obj_device = ManagerPhoto.objects.filter(device_folder_id=device_id)[0]
        re_dict = {}
        re_dict['id'] = obj_device.device_folder_id
        re_dict['name'] = obj_device.device_folder_name
        re_list.append(re_dict)

    # return HttpResponse(json.dumps(re_list))
    return render_to_response(template, {'devicelist': re_list},
                              context_instance=RequestContext(request))


def photo_dir(request):
    template = 'photo_dir.html'

    device_id = request.GET.get('device_id')
    if not device_id:
        device_id = request.POST.get('device_id')

    re_list = []
    objs_video = ManagerPhoto.objects.filter(device_folder_id=device_id)

    for video in objs_video:
        re_dict = {}
        re_dict['id'] = video.type_folder_id
        re_dict['name'] = video.type_folder_name
        re_list.append(re_dict)

    re_list_new = []
    [re_list_new.append(i) for i in re_list if not i in re_list_new]
    # return HttpResponse(json.dumps(re_list_new))
    return render_to_response(template, {'typelist': re_list_new, 'device_id':device_id},
                              context_instance=RequestContext(request))


def photo_gallery(request):
    template = 'photo_gallery.html'

    device_id = request.GET.get('device_id')
    if not device_id:
        device_id = request.POST.get('device_id')
    type_id = request.GET.get('type_id')
    if not type_id:
        type_id = request.POST.get('type_id')

    re_list = []
    objs_photo = ManagerPhoto.objects.filter(device_folder_id=device_id, type_folder_id=type_id)
    for photo in objs_photo:
        re_dict = {}
        re_dict['id'] = photo.id
        re_dict['name'] = photo.name
        re_dict['size'] = photo.size
        re_dict['time'] = photo.date_time
        re_dict['path'] = '/'+photo.device_folder_id+'/'+photo.type_folder_id+'/'+photo.small_name

        re_list.append(re_dict)

    re_list_new = []
    [re_list_new.append(i) for i in re_list if not i in re_list_new]
    # return HttpResponse(json.dumps(re_list_new))
    return render_to_response(template, {'filelist': re_list_new, 'device_id':device_id, 'type_id':type_id},
                              context_instance=RequestContext(request))

def do_file(request):
    copy.doFile()
    return HttpResponse("doFile finish")


def start_power_timer(request):
    t = threading.Timer(5, power_timer)
    t.start()
    return HttpResponse("start_power_timer finish")

import testInput
def power_timer():
    print 'timer.......'
    testInput.testDeviceInput()

    # if curr_device != '':
    #     #检测电量（无数据&iphone和android电量满）
    #     b_anroid = get_android_power_b()
    #     b_iphone = get_iphone_power_b()
    #     if b_anroid and b_iphone:
    #         relay.turn_off()

    t = threading.Timer(5, power_timer)
    t.start()

def get_android_power(request):
    str = deviceControl.getAndroidPower()
    return HttpResponse("The power of Android is:" + str)

def get_android_power_b():
    str = deviceControl.getAndroidPower()
    return str

def get_iphone_power(request):
    str = deviceControl.getIphonePower()
    return HttpResponse("The power of Iphone is:" + str)

def get_iphone_power_b():
    str = deviceControl.getIphonePower()
    return str
'''
获取deviceid文件夹
'''
def getDeviceList_Video(request):
    template = ''

    objs_device = ManagerVideo.objects.all().values('device_folder_id').distinct()

    re_list = []
    for device in objs_device:
        device_id = device['device_folder_id']
        obj_device = ManagerVideo.objects.filter(device_folder_id=device_id)[0]
        re_dict = {}
        re_dict['id'] = obj_device.device_folder_id
        re_dict['name'] = obj_device.device_folder_name
        re_list.append(re_dict)

    # return HttpResponse(json.dumps(re_list))
    return render_to_response(template, {'devicelist': re_list},
                              context_instance=RequestContext(request))
'''
根据deviceid获取类型文件夹
'''
def getTypeList_Video(request):
    template = ''

    device_id = request.GET.get('device_id')
    if not device_id:
        device_id = request.POST.get('device_id')

    re_list = []
    objs_video = ManagerVideo.objects.filter(device_folder_id=device_id)
    for video in objs_video:
        re_dict = {}
        re_dict['id'] = video.type_folder_id
        re_dict['name'] = video.type_folder_name
        re_list.append(re_dict)

    re_list_new = []
    [re_list_new.append(i) for i in re_list if not i in re_list_new]
    # return HttpResponse(json.dumps(re_list_new))
    return render_to_response(template, {'typelist': re_list_new},
                              context_instance=RequestContext(request))

'''
根据deviceid和类型文件夹Id获取文件
'''
def getFilesList_Video(request):
    template = ''

    device_id = request.GET.get('device_id')
    if not device_id:
        device_id = request.POST.get('device_id')
    folder_id = request.GET.get('folder_id')
    if not folder_id:
        folder_id = request.POST.get('folder_id')

    re_list = []
    objs_video = ManagerVideo.objects.filter(device_folder_id=device_id, type_folder_id=folder_id)
    for video in objs_video:
        re_dict = {}
        re_dict['name'] = video.name
        re_dict['size'] = video.size
        re_dict['time'] = video.date_time
        re_dict['path'] = '/'+video.device_folder_id+'/'+video.type_folder_id+'/'+video.name

        re_list.append(re_dict)

    re_list_new = []
    [re_list_new.append(i) for i in re_list if not i in re_list_new]
    # return HttpResponse(json.dumps(re_list_new))
    return render_to_response(template, {'filelist': re_list_new},
                              context_instance=RequestContext(request))

'''
获取deviceid文件夹
'''
def getDeviceList_Photo(request):
    template ='mobile.html'

    objs_device = ManagerPhoto.objects.all().values('device_folder_id').distinct()

    re_list = []
    for device in objs_device:
        device_id = device['device_folder_id']
        obj_device = ManagerPhoto.objects.filter(device_folder_id=device_id)[0]
        re_dict = {}
        re_dict['id'] = obj_device.device_folder_id
        re_dict['name'] = obj_device.device_folder_name
        re_list.append(re_dict)

    # return HttpResponse(json.dumps(re_list))
    return render_to_response(template, {'devicelist': re_list},
                              context_instance=RequestContext(request))

'''
根据deviceid获取类型文件夹
'''
def getTypeList_Photo(request):
    template = 'photo_dir.html'

    device_id = request.GET.get('device_id')
    if not device_id:
        device_id = request.POST.get('device_id')

    re_list = []
    objs_video = ManagerPhoto.objects.filter(device_folder_id=device_id)
    for video in objs_video:
        re_dict = {}
        re_dict['id'] = video.type_folder_id
        re_dict['name'] = video.type_folder_name
        re_list.append(re_dict)

    re_list_new = []
    [re_list_new.append(i) for i in re_list if not i in re_list_new]
    # return HttpResponse(json.dumps(re_list_new))
    return render_to_response(template, {'typelist': re_list_new, 'device_id':device_id},
                              context_instance=RequestContext(request))

'''
根据deviceid和类型文件夹Id获取文件
'''
def getFilesList_Photo(request):
    template = 'photo_gallery.html'

    device_id = request.GET.get('device_id')
    if not device_id:
        device_id = request.POST.get('device_id')
    type_id = request.GET.get('type_id')
    if not type_id:
        type_id = request.POST.get('type_id')

    re_list = []
    objs_photo = ManagerPhoto.objects.filter(device_folder_id=device_id, type_folder_id=type_id)
    for photo in objs_photo:
        re_dict = {}
        re_dict['id'] = photo.id
        re_dict['name'] = photo.name
        re_dict['size'] = photo.size
        re_dict['time'] = photo.date_time
        re_dict['path'] = '/'+photo.device_folder_id+'/'+photo.type_folder_id+'/'+photo.name

        re_list.append(re_dict)

    re_list_new = []
    [re_list_new.append(i) for i in re_list if not i in re_list_new]
    # return HttpResponse(json.dumps(re_list_new))
    return render_to_response(template, {'filelist': re_list_new},
                              context_instance=RequestContext(request))

def getFilesList_Photo(device_id, type_id):
    re_list = []
    objs_photo = ManagerPhoto.objects.filter(device_folder_id=device_id, type_folder_id=type_id)
    for photo in objs_photo:
        re_dict = {}
        re_dict['id'] = photo.id
        re_dict['name'] = photo.name
        re_dict['size'] = photo.size
        re_dict['time'] = photo.date_time
        re_dict['path'] = '/'+photo.device_folder_name+'/'+photo.type_folder_id+'/'+photo.name

        re_list.append(re_dict)

    re_list_new = []
    [re_list_new.append(i) for i in re_list if not i in re_list_new]
    # return HttpResponse(json.dumps(re_list_new))
    return re_list_new

'''
根据deviceid和类型文件夹Id获取小图片文件
'''
def getSmallFilesList_Photo(request):
    template = ''

    device_id = request.GET.get('device_id')
    if not device_id:
        device_id = request.POST.get('device_id')
    type_id = request.GET.get('type_id')
    if not type_id:
        type_id = request.POST.get('type_id')

    re_list = []
    objs_video = ManagerPhoto.objects.filter(device_folder_id=device_id, type_folder_id=type_id)
    for video in objs_video:
        re_dict = {}
        re_dict['name'] = video.name
        re_dict['size'] = video.size
        re_dict['time'] = video.date_time
        re_dict['path'] = '/'+video.device_folder_id+'/'+video.type_folder_id+'/'+video.small_name

        re_list.append(re_dict)

    re_list_new = []
    [re_list_new.append(i) for i in re_list if not i in re_list_new]
    # return HttpResponse(json.dumps(re_list_new))
    return render_to_response(template, {'smallfilelist': re_list_new},
                              context_instance=RequestContext(request))

'''
根据设备ID获取日期
'''
def get_date_by_deviceid(device_id):
    obj_device = ManagerDevice.objects.filter(device_id=device_id)[0]
    return obj_device.date

'''
写入设备信息
'''
def insert_data_device(dict_data):

    if dict_data.has_key('device_id'):
        device_id = dict_data['device_id']
    else:
        device_id = None
    if dict_data.has_key('date'):
        date = dict_data['date']
    else:
        date = None

    c = ManagerDevice(device_id=device_id,
                      date=date)
    c.save()

'''
写入视频信息
'''
def insert_data_video(dict_data):
    c = ManagerVideo(dict_data)
    c.save()

'''
写入视频信息
'''
def insert_data_photo(dict_data):

    if dict_data.has_key('device_folder_id'):
        device_folder_id = dict_data['device_folder_id']
    else:
        device_folder_id = None
    if dict_data.has_key('device_folder_name'):
        device_folder_name = dict_data['device_folder_name']
    else:
        device_folder_name = None
    if dict_data.has_key('type_folder_id'):
        type_folder_id = dict_data['type_folder_id']
    else:
        type_folder_id = None
    if dict_data.has_key('type_folder_name'):
        type_folder_name = dict_data['type_folder_name']
    else:
        type_folder_name = None
    if dict_data.has_key('small_name'):
        small_name = dict_data['small_name']
    else:
        small_name = None
    if dict_data.has_key('name'):
        name = dict_data['name']
    else:
        name = None
    if dict_data.has_key('path'):
        path = dict_data['path']
    else:
        path = None
    if dict_data.has_key('date_time'):
        date_time = dict_data['date_time']
    else:
        date_time = None

    c = ManagerPhoto(
        device_folder_id=device_folder_id,
        device_folder_name=device_folder_name,
        type_folder_id=type_folder_id,
        type_folder_name=type_folder_name,
        small_name=small_name,
        name=name,
        path=path,
        date_time=date_time,
        )
    c.save()

'''
电源满时处理
'''
def power_satiate():

    # 断掉继电器

    # 页面显示
    pass

'''
触发播放视频处理
'''
def play_video():

    #根据条件获取文件路径
    update_page_status('video')

    # 页面播放
    pass

'''
触发播放图片处理
'''
def display_photo(request):
    template = 'play_photo.html'

    device_id = request.GET.get('device_id')
    if not device_id:
        device_id = request.POST.get('device_id')
    type_id = request.GET.get('type_id')
    if not type_id:
        type_id = request.POST.get('type_id')
    #
    # #根据条件获取文件路径
    update_page_status('photo')

    #获取image List
    sliders = getFilesList_Photo(device_id, type_id)

    # 页面播放
    return render_to_response(template,{'sliders':sliders},
                              context_instance=RequestContext(request))

'''
触发播放图片
'''
def play_photo(request):
    device_id = request.GET.get('device_id')
    if not device_id:
        device_id = request.POST.get('device_id')
    type_id = request.GET.get('type_id')
    if not type_id:
        type_id = request.POST.get('type_id')

    #根据条件获取文件路径
    update_page_status('photo;'+ device_id + ';' + type_id)

    return HttpResponse("success")

'''
停止图片播放
'''
def stop_photo(request):

    update_page_status('idle')
    return HttpResponse("success")

'''
停止图片播放
'''
def end_photo(request):
    template = 'index.html'

    update_page_status('idle')
    return render_to_response(template, context_instance=RequestContext(request))

def play_game(request):
    deviceControl.startGame()
    return HttpResponse("play game success");


def stop_game(request):
    deviceControl.stopGame()
    return HttpResponse("stop game success");


'''
查看当前页面状态
'''
def get_page_status():

    #获取页面状态信息
    status_key = 'page_status'
    try:
        obj_status = ManagerStatus.objects.filter(type=status_key)[0]
    except:
        return 'idle'
    return obj_status.status

'''
查看数据写状态
'''
def get_data_status():

    #获取页面状态信息
    status_key = 'data_status'
    try:
        obj_status = ManagerStatus.objects.filter(type=status_key)[0]
    except:
        return True
    return obj_status.status

'''
查看设备状态
'''
def get_device_status():

    #获取页面状态信息
    status_key = 'device_status'
    try:
        obj_status = ManagerStatus.objects.filter(type=status_key)[0]
    except:
        return 'idle'
    return obj_status.status

'''
update当前页面状态
idle：空闲， video：视屏播放中， photo：图片播放中
'''
def update_page_status(status):
    #更新页面状态信息
    status_key = 'page_status'

    try:
        obj_sta = ManagerStatus.objects.filter(type=status_key)
        if obj_sta.count() is 0:
            obj = ManagerStatus(type=status_key, status=status)
            obj.save()
        else:
            obj_status = obj_sta[0]
            obj_status.status = status
            obj_status.save()
    except:
        return False

    return True

'''
update当前是否有数据传输
idle：空闲
'''
def update_data_status(status):
    #更新页面状态信息
    status_key = 'data_status'

    try:
        obj_sta = ManagerStatus.objects.filter(type=status_key)
        if obj_sta.count() is 0:
            obj = ManagerStatus(type=status_key, status=status)
            obj.save()
        else:
            obj_status = obj_sta[0]
            obj_status.status = status
            obj_status.save()
    except:
        return False

    return True

'''
update设备信息
'''
def update_device_status(status):
    #更新页面状态信息
    status_key = 'device_status'

    try:
        obj_sta = ManagerStatus.objects.filter(type=status_key)
        if obj_sta.count() is 0:
            obj = ManagerStatus(type=status_key, status=status)
            obj.save()
        else:
            obj_status = obj_sta[0]
            obj_status.status = status
            obj_status.save()
    except:
        return False

    return True


#-------------------------------------------

'''
获取视频信息
'''
def get_video_info(request):
    device_id = request.GET.get('device_id')
    if not device_id:
        device_id = request.POST.get('device_id')
    name = request.GET.get('name')
    if not name:
        name = request.POST.get('name')
    area = request.GET.get('area')
    if not area:
        area = request.POST.get('area')
    path = request.GET.get('path')
    if not path:
        path = request.POST.get('path')
    date = request.GET.get('date')
    if not date:
        date = request.POST.get('date')
    kwargs = {}
    if device_id:
        kwargs['device_id'] = device_id
    if name:
        kwargs['name'] = name
    if area:
        kwargs['area'] = area
    if path:
        kwargs['path'] = path
    if date:
        kwargs['date_time'] = date

    objs_video = ManagerVideo.objects.filter(**kwargs)
    return HttpResponse(simplejson.loads(serialize('json',objs_video)))

def page_timer_to_index(request):
    page_status = get_page_status()
    if page_status == 'idle':
        return render_to_response('/index/')
    else:
        return HttpResponse('')

def page_timer_to_photo(request):

    page_status = get_page_status()
    if page_status != 'idle':
        return HttpResponseRedirect('/play_photo/')
    else:
        return HttpResponse('')

def play_photo(request):
    template = 'play_photo.html'
    page_status = get_page_status()
    sta_list = page_status.split(';')

    device_id = sta_list[1]
    type_id = sta_list[2]

    update_page_status('idle')
    #获取image List
    sliders = getFilesList_Photo(device_id, type_id)

    # 页面播放
    return render_to_response(template,{'sliders':sliders},
                              context_instance=RequestContext(request))


def get_battery_android(request):
    return HttpResponse(deviceControl.getAndroidPower());

def get_battery_iphone(request):
    return HttpResponse(deviceControl.getIphonePower())