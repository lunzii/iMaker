# -*- coding:utf-8 -*-

from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from manager.core import views
from manager.mobile import views as mobile

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),


    # --------------------health-----------------------
    # url(r'^index/', views.index),
    url(r'^$', views.index),
    #url(r'^index/', TemplateView.as_view(template_name='base.html')),
    #url(r'^insert_data_video/', views.insert_data_video),
    #url(r'^insert_data_photo/', views.insert_data_video),
    #url(r'^photo_dir/', views.photo_dir),
    #url(r'^photo_gallery/', views.photo_gallery),
    #url(r'^game_show/', TemplateView.as_view(template_name='game_show.html')),
    #url(r'^game_show_mario/', TemplateView.as_view(template_name='game_show_mario.html')),
    #url(r'^game_show_konglong/', TemplateView.as_view(template_name='game_show_konglong.html')),
    #url(r'^do_file/', views.do_file),
    #
    #url(r'^power_timer/', views.power_timer),
    #url(r'^android_power/', views.get_android_power),
    #url(r'^iphone_power/', views.get_iphone_power),
    #
    #url(r'^play_photo/', views.play_photo),
    #url(r'^display_photo/', views.display_photo),
    #url(r'^stop_photo/', views.stop_photo),
    #url(r'^end_photo/', views.end_photo),
    #
    #url(r'^play_game/', views.play_game),
    #url(r'^stop_game/', views.stop_game),
    #
    #url(r'^play_photo/', views.play_photo),
    #
    #url(r'^start_power_timer/', views.start_power_timer),
    #
    #url(r'^page_timer_to_index/', views.page_timer_to_index),
    #url(r'^page_timer_to_photo/', views.page_timer_to_photo),
    #
    #url(r'^get_battery_android/', views.get_battery_android),
    #url(r'^get_battery_iphone/', views.get_battery_iphone),

    #--------------------
    url(r'^m/$', mobile.index),
    url(r'^m_family/$', mobile.family),
    url(r'^m_share/$', mobile.share),
    url(r'^m_me/$', mobile.me),


    #静态文件资源路径
    url(r'^%s/(?P<path>.*)$' % settings.STATIC_URL.replace('/',''), 'django.views.static.serve', {'document_root':settings.STATIC_ROOT}),
    url(r'^%s/(?P<path>.*)$' % settings.MEDIA_URL.replace('/',''), 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
    url(r'^%s/(?P<path>.*)$' % settings.RES_URL.replace('/',''), 'django.views.static.serve', {'document_root':settings.RES_ROOT}),

)
