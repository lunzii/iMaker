# -*- coding:utf-8 -*-

from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from manager.core import views, BoxInterface as bi_views, AppInterface as ai_views
from manager.mobile import views as mobile

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),


    # 处理盒子请求
    url(r'^get_import_time/', bi_views.get_import_time),
    url(r'^save_pic_to_server/', bi_views.save_pic_to_server),

    # 处理APP请求
    url(r'^get_pic_info/', ai_views.get_pic_info),
    url(r'^delete_pic_info/', ai_views.delete_pic_info),

    #--------------------
    url(r'^m/$', mobile.index),


    #静态文件资源路径
    url(r'^%s/(?P<path>.*)$' % settings.STATIC_URL.replace('/',''), 'django.views.static.serve', {'document_root':settings.STATIC_ROOT}),
    url(r'^%s/(?P<path>.*)$' % settings.MEDIA_URL.replace('/',''), 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
    url(r'^%s/(?P<path>.*)$' % settings.RES_URL.replace('/',''), 'django.views.static.serve', {'document_root':settings.RES_ROOT}),

)
