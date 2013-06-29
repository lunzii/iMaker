# -*- coding:utf-8 -*-
'''
Created on 13-6-29

@author:
'''

from django.db import models


class Water(models.Model):
    start_time = models.DateTimeField(null=True,blank=True,verbose_name='开始时间')
    end_time = models.DateTimeField(null=True,blank=True,verbose_name='结束时间')
    status = models.CharField(null=True,blank=True,max_length=512,verbose_name='提醒状态')

    class Meta:
        verbose_name = '喝水提醒记录'
        verbose_name_plural = '喝水提醒记录'
        db_table = 'health_manager_water'

class Sport(models.Model):
    start_time = models.DateTimeField(null=True,blank=True,verbose_name='开始时间')
    end_time = models.DateTimeField(null=True,blank=True,verbose_name='结束时间')
    temp_time = models.DateTimeField(null=True,blank=True,verbose_name='临时时间')
    status = models.CharField(null=True,blank=True,max_length=512,verbose_name='提醒状态')

    class Meta:
        verbose_name = '运动提醒记录'
        verbose_name_plural = '运动提醒记录'
        db_table = 'health_manager_sport'