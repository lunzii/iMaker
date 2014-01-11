# -*- coding:utf-8 -*-
'''
Created on 13-6-29

@author:team
'''

from django.db import models

class ManagerDevice(models.Model):
    name = models.CharField(null=True,blank=True,max_length=128,verbose_name='设备名称')
    device_id = models.CharField(null=True,blank=True,max_length=128,db_index=True,verbose_name='设备唯一ID')
    date = models.DateTimeField(null=True,blank=True,verbose_name='注册时间')

    class Meta:
        verbose_name = '设备信息'
        verbose_name_plural = '设备信息'
        db_table = 'manager_device'

class ManagerPhoto(models.Model):
    device_folder_id = models.CharField(null=True,blank=True,max_length=128,db_index=True,verbose_name='设备唯一ID')
    device_folder_name = models.CharField(null=True,blank=True,max_length=128,db_index=True,verbose_name='设备唯一ID')

    type_folder_id = models.CharField(null=True,blank=True,max_length=128,verbose_name='类型文件夹ID')
    type_folder_name = models.CharField(null=True,blank=True,max_length=128,verbose_name='类型文件夹名称')

    small_name = models.CharField(null=True,blank=True,max_length=128,verbose_name='小照片名称')
    name = models.CharField(null=True,blank=True,max_length=128,verbose_name='照片名称')
    size = models.CharField(null=True,blank=True,max_length=128,verbose_name='照片大小')
    area = models.CharField(null=True,blank=True,max_length=128,verbose_name='照片地区')
    path = models.CharField(null=True,blank=True,max_length=128,verbose_name='存储地址')
    date_time = models.CharField(null=True,blank=True,max_length=128,verbose_name='时间')

    note = models.CharField(null=True,blank=True,max_length=128,verbose_name='任何描述')

    class Meta:
        verbose_name = '照片信息'
        verbose_name_plural = '照片信息'
        db_table = 'manager_photo'

class ManagerVideo(models.Model):
    device_folder_id = models.CharField(null=True,blank=True,max_length=128,db_index=True,verbose_name='设备唯一ID')
    device_folder_name = models.CharField(null=True,blank=True,max_length=128,db_index=True,verbose_name='设备唯一ID')

    type_folder_id = models.CharField(null=True,blank=True,max_length=128,verbose_name='类型文件夹ID')
    type_folder_name = models.CharField(null=True,blank=True,max_length=128,verbose_name='类型文件夹名称')

    name = models.CharField(null=True,blank=True,max_length=128,verbose_name='视频名称')
    size = models.CharField(null=True,blank=True,max_length=128,verbose_name='视频大小')
    area = models.CharField(null=True,blank=True,max_length=128,verbose_name='视频地区')
    path = models.CharField(null=True,blank=True,max_length=128,verbose_name='存储地址')
    date_time = models.CharField(null=True,blank=True,max_length=128,verbose_name='时间')

    note = models.CharField(null=True,blank=True,max_length=128,verbose_name='任何描述')

    class Meta:
        verbose_name = '视频信息'
        verbose_name_plural = '视频信息'
        db_table = 'manager_video'

class ManagerStatus(models.Model):
    type = models.CharField(null=True,blank=True,max_length=128,verbose_name='类型')
    status = models.CharField(null=True,blank=True,max_length=128,verbose_name='类型状态')

    class Meta:
        verbose_name = '类型状态'
        verbose_name_plural = '类型状态'
        db_table = 'manager_status'

class ManagerDevice(models.Model):
    device_id = models.CharField(null=True,blank=True,max_length=128,verbose_name='ID')
    date = models.CharField(null=True,blank=True,max_length=128,verbose_name='日期')

    class Meta:
        verbose_name = '类型状态'
        verbose_name_plural = '类型状态'
        db_table = 'manager_status'