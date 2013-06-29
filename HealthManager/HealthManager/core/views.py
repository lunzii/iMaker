# -*- coding:utf-8 -*-
'''
Created on 13-6-29

@author: Joys
'''
import datetime,httplib
import urllib2
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils import simplejson

from HealthManager.core.models import Water,Sport


def index(request):
    obj_water_all = Water.objects.all()
    obj_sport_all = Sport.objects.all()

    # -----------------------获取 天气------------------------
    weather_info_dict = get_weather()


    # -------------获取 温度、湿度、空气质量、粉尘质量---------


    # -------------------------处理喝水逻辑------------------
    cur_water_status = True
    cur_time = datetime.datetime.now()
    water_status_true = obj_water_all.filter(end_time=None).order_by('-start_time')
    if cur_water_status:
        if len(water_status_true) > 0:
            water_status_true = water_status_true[0]
            start_time_val = water_status_true.start_time
            start_time_val = datetime.datetime.strptime(str(start_time_val)[0:19], '%Y-%m-%d %H:%M:%S')
            seconds_w = (cur_time - start_time_val).seconds
            if seconds_w > 60 * 60:
                # --- 提醒该喝水啦 ---

                #已经提醒 本次结束， 重新计数
                water_status_true.end_time = cur_time
                water_status_true.status = 'True'
                water_status_true.save()
            else:
                pass
        else:
            obj_water = Water(start_time=cur_time)
            obj_water.save()
    else:
        if len(water_status_true) > 0:
            #水杯已不在 本次结束， 重新计数
            water_status_true.end_time = cur_time
            water_status_true.status = 'True'
            water_status_true.save()


    # -------------------------处理运动逻辑-------------------
    cur_sport_status = True
    cur_time = datetime.datetime.now()
    sport_status_true = obj_sport_all.filter(end_time=None).order_by('-start_time')
    if cur_sport_status:
        if len(sport_status_true) > 0:
            sport_status_true = sport_status_true[0]
            start_time_val = sport_status_true.start_time
            start_time_val = datetime.datetime.strptime(str(start_time_val)[0:19], '%Y-%m-%d %H:%M:%S')

            seconds_s = (cur_time - start_time_val).seconds
            if seconds_s > 60 * 60:
                # --- 判断时间段 ---
                if cur_time.hour > 6 and cur_time.hour < 10:
                    #--- 来段体操 ---
                    pass
                elif cur_time.hour >=10 and cur_time.hour < 12:
                    #--- 来段眼保健操 ---
                    pass
                elif cur_time.hour >= 14 and cur_time.hour <18:
                    #--- 需要伸展一下了 ---
                    pass

                #已经提醒 本次结束， 重新计数
                sport_status_true.end_time = cur_time
                sport_status_true.status = 'True'
                sport_status_true.save()
        else:
            # --- 检测到有人但数据没有记录时，增加记录---
            obj_sport = Sport(start_time=cur_time)
            obj_sport.save()
    else:
        if len(sport_status_true) > 0:
            sport_status_true = sport_status_true[0]
            sport_temptime = sport_status_true.filter(temp_time=None)

            if len(sport_temptime) > 0:
                sport_status_true.temp_time = cur_time
                sport_status_true.save()
            else:
                #---判断是否为短暂离开---
                sport_temptime_val = sport_status_true.temp_time
                seconds = (cur_time - sport_temptime_val).seconds

                if seconds > 60:
                    # 非短暂离开，结束本次
                    sport_status_true.end_time = cur_time
                    sport_status_true.status = 'True'
                    sport_status_true.save()
                else:
                    #短暂离开， 忽略
                    pass
        else:
            # 人不再，也没有记录 忽略
            pass

    return render_to_response('index.html',{},
                              context_instance=RequestContext(request))
'''
获取天气情况
'''
def get_weather():
    req = urllib2.Request('http://m.weather.com.cn/data/101280601.html')
    response = urllib2.urlopen(req)
    the_page = response.read()
    dictinfo = simplejson.loads(the_page)
    weatherinfo = dictinfo['weatherinfo']

    weather_dict={}

    weather_dict['city'] = weatherinfo['city'].encode('utf-8')
    weather_dict['date_y'] = weatherinfo['date_y'].encode('utf-8')
    weather_dict['temperature'] = weatherinfo['temp1'].encode('utf-8')
    weather_dict['desc'] = weatherinfo['weather1'].encode('utf-8')
    img_num = weatherinfo['img1'].encode('utf-8')
    weather_dict['img_url'] = 'http://m.weather.com.cn/img/c' + img_num + '.gif'

    return weather_dict