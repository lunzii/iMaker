# -*- coding:utf-8 -*-

from django.conf.urls import patterns, include, url

import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from HealthManager.core import views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'HealthManager.views.home', name='home'),
    # url(r'^HealthManager/', include('HealthManager.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),


    # --------------------health-----------------------
    url(r'^index/', views.index),

    #静态文件资源路径
    url(r'^%s/(?P<path>.*)$' % settings.STATIC_URL.replace('/',''), 'django.views.static.serve', {'document_root':settings.STATIC_ROOT}),
    url(r'^%s/(?P<path>.*)$' % settings.MEDIA_URL.replace('/',''), 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
    url(r'^%s/(?P<path>.*)$' % settings.RES_URL.replace('/',''), 'django.views.static.serve', {'document_root':settings.RES_ROOT}),

)
