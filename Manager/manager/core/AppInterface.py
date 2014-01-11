# -*- coding:utf-8 -*-
'''
Created on 13-6-29

@author:
'''
import os
from django.core.serializers import json
from django.http import HttpResponse
from django.utils import simplejson

from manager.core.models import FreePicInfo

"""
处理APP的请求，返回数据
"""
def get_pic_info(request):
    time = request.GET.get('time')
    if not time:
        time = request.POST.get('time')
    user_name = request.GET.get('user_name')
    if not user_name:
        user_name = request.POST.get('user_name')

    print time,user_name

    # 检索时间前100条记录，需用户名匹配
    pic_oj = FreePicInfo.objects.filter(user_name=user_name, pic_date__lte=time)[:100]

    # 区分有备注和没有备注的数据
    note_str = []
    note_null = []

    for pic_o in list(pic_oj):
        if pic_o.pic_note is None:
            note_null.append(pic_o)
        else:
            note_str.append(pic_o)

    pic_total_l = []

    # ---处理有备注的情况---
    note_str_list = []
    note_list = pic_oj.values('pic_note')
    for note_v in note_list:
        note_val = note_v['pic_note']
        if not note_val in note_str_list and not note_val is None:
            note_str_list.append(note_val)

    for note_str_val in note_str_list:
        dict_item_pic = {'note': note_str_val}
        pic_note_l = get_pic_by_note(note_str, note_str_val)
        data_list = []
        for pic_note in pic_note_l:
            dict_pic_info = {'md5': pic_note.pic_md5, 'username': pic_note.user_name, 'url': pic_note.pic_path,
                             'time': pic_note.pic_date}
            data_list.append(dict_pic_info)
        dict_item_pic['data'] = data_list

        pic_total_l.append(dict_item_pic)

    # ---处理无备注的情况---
    note_null_list = []
    for note_oj in note_null:
        pic_date_v = str(note_oj.pic_date).split(" ")[0]
        if not pic_date_v in note_null_list and not pic_date_v is None:
            note_null_list.append(pic_date_v)

    for note_null_val in note_null_list:
        dict_item_pic_null = {}
        dict_item_pic_null['time'] = note_null_val
        pic_null_l = get_pic_by_note_null(note_null, note_null_val)
        data_list_null = []
        for pic_null in pic_null_l:
            dict_pic_info_null = {'md5': pic_null.pic_md5, 'username': pic_null.user_name, 'url': pic_null.pic_path,
                             'time': pic_null.pic_date}
            data_list_null.append(dict_pic_info_null)
        dict_item_pic_null['data'] = data_list_null

        pic_total_l.append(dict_item_pic_null)

    return HttpResponse(simplejson.dumps(pic_total_l))


def get_pic_by_note(obj_pic_l, note_val):
    pic_value_oj = []
    for obj_pic in obj_pic_l:
        if obj_pic.pic_note == note_val:
            pic_value_oj.append(obj_pic)
    return pic_value_oj

def get_pic_by_note_null(obj_pic_l, note_val):
    pic_value_oj = []
    for obj_pic in obj_pic_l:
        if note_val in obj_pic.pic_date:
            pic_value_oj.append(obj_pic)
    return pic_value_oj


"""
根据md5删除指定图片
"""
def delete_pic_info(request):
    md5 = request.GET.get('md5')
    if not md5:
        md5 = request.POST.get('md5')

    try:
        pic_oj = FreePicInfo.objects.filter(pic_md5=md5)[0]
        pic_oj.delete()
    except:
        return HttpResponse('error')

    return HttpResponse('success')





