# -*- coding:utf-8 -*-
'''
Created on 14-1-11

@author: olunxchen
'''

from django.shortcuts import render_to_response


def index(request):
    return render_to_response('m_index.html')


def family(request):
    return render_to_response('m_family.html')