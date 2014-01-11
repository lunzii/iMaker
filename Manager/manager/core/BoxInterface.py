# -*- coding:utf-8 -*-
'''
Created on 13-6-29

@author:
'''
import os
import zipfile
from django.http import HttpResponse
import time
from django.views.decorators.csrf import csrf_exempt
from manager import settings

from manager.core.models import FreePicInfo
# from PIL import Image
# from PIL.ExifTags import TAGS

"""
返回给盒子最后拷贝的时间。根据照片最后时间
"""
def get_import_time(request):

    try:
        device_id = request.GET.get('device_id')
        if not device_id:
            device_id = request.POST.get('device_id')
        user_name = request.GET.get('user_name')
        if not user_name:
            user_name = request.POST.get('user_name')

        pic_oj = FreePicInfo.objects.filter(device_id=device_id, user_name=user_name).order_by('-pic_date')
        last_pic_date = pic_oj[0].pic_date

        return HttpResponse(str(last_pic_date))

    except:

        return HttpResponse("error")

"""
接收盒子的请求，解压图片保存到图片信息到数据库
"""
@csrf_exempt
def save_pic_to_server(request):

    box_id = request.POST.get('box_id')
    device_id = request.POST.get('device_id')
    user_name = request.POST.get('user_name')

    # 定义保存目录
    curr_time = time.strftime('%Y-%m-%d %H-%M-%S', time.localtime(time.time()))
    pro_root = settings.PRO_ROOT + settings.RES_URL
    store_path = pro_root + curr_time

    # 存储文件到指定目录
    if len(request.FILES) > 0:
        file_name = str(device_id) + str(user_name) + ".zip"
        handle_uploaded_file(request.FILES['pic_file'], store_path, file_name)

        # 文件解压
        unzip(os.path.join(store_path, file_name))


    # 循环读取，文件信息写入数据库
    temp = str(device_id) + str(user_name)
    rootdir = os.path.join(store_path, temp)
    for parent, dirnames, filenames in os.walk(rootdir):   # 三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
        for filename in filenames:
            filename_path = os.path.join(parent, filename)

            pic_md5 = get_md5_str(filename_path)
            pic_size = os.path.getsize(filename_path)
            try:
                pic_date = get_exif_data(filename_path)['DateTimeOriginal']
            except:
                pass

            # 写入数据库
            pic_path = os.path.join(os.path.join(settings.RES_URL + curr_time, temp), filename)
            print pic_path
            pic_data = FreePicInfo(box_id=2, device_id=device_id, user_name=user_name, pic_md5=pic_md5, pic_date=pic_date,
                                   pic_size=pic_size, pic_path=pic_path, write_date=curr_time)
            pic_data.save()

    return HttpResponse('success')


"""
文件保存目录
"""
def handle_uploaded_file(f, store_path, file_name):
    if not os.path.exists(store_path):
        os.makedirs(store_path)

    file_path = os.path.join(store_path, file_name)  # 完整路径名
    destination = open(file_path, 'wb+')
    for chunk in f.chunks():
        destination.write(chunk)

    destination.close()

    return file_path


"""
获取文件MD5值
"""
def get_md5_str(file):
    from hashlib import md5
    m = md5()
    # 需要使用二进制格式读取文件内容
    a_file = open(file, 'rb')
    m.update(a_file.read())
    return m.hexdigest()

"""
获取图片的exif信息
"""
# def get_exif_data(fname):
#     ret = {}
#     try:
#         img = Image.open(fname)
#         if hasattr(img, '_getexif'):
#             exifinfo = img._getexif()
#             if not exifinfo is None:
#                 for tag, value in exifinfo.items():
#                     decoded = TAGS.get(tag, tag)
#                     ret[decoded] = value
#     except IOError:
#         print 'IOERROR ' + fname
#     return ret

"""
解压文件到当前目录
"""
def unzip(s_zip):
    save_path = s_zip[:-4]
    zipfile.ZipFile(s_zip).extractall(save_path)
