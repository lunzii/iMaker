# -*- coding:utf-8 -*-
'''
Created on 13-6-29

@author:
'''
import threading
<<<<<<< HEAD
import copy
=======
>>>>>>> ios
from django.core.serializers import serialize
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils import simplejson
from manager.core.models import ManagerVideo, ManagerPhoto, ManagerStatus, ManagerDevice

def index(request):
        return render_to_response('test.html')
