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

class FreePicInfo(models.Model):
    box_id = models.CharField(null=True,blank=True,max_length=128,db_index=True,verbose_name='盒子唯一ID')
    device_id = models.CharField(null=True,blank=True,max_length=128,db_index=True,verbose_name='设备唯一ID')

    user_name = models.CharField(null=True,blank=True,max_length=128,verbose_name='用户名')
    write_date = models.CharField(null=True,blank=True,max_length=128,verbose_name='写入数据时间')

    pic_date = models.CharField(null=True,blank=True,max_length=128,verbose_name='图片日期')
    pic_size = models.CharField(null=True,blank=True,max_length=128,verbose_name='图片大小')
    pic_md5 = models.CharField(null=True,blank=True,max_length=128,verbose_name='图md5值')
    pic_path = models.CharField(null=True,blank=True,max_length=128,verbose_name='图片存储路径')

    pic_loc_ctr = models.CharField(null=True,blank=True,max_length=128,verbose_name='图片地区-国家')
    pic_loc_p = models.CharField(null=True,blank=True,max_length=128,verbose_name='图片地区-省')
    pic_loc_city = models.CharField(null=True,blank=True,max_length=128,verbose_name='图片地区-市')
    pic_loc_area = models.CharField(null=True,blank=True,max_length=128,verbose_name='图片地区-详细地区')

    pic_note = models.CharField(null=True,blank=True,max_length=128,verbose_name='图片描述')

    class Meta:
        db_table = 'free_pic_info'