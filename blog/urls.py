from django.conf.urls import url
from . import views
from .views import *

urlpatterns = [

    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/pgmnote/$', views.post_pgmnote, name='post_pgmnote'),

    url(r'^post/device/$', views.post_devicelist, name='post_devicelist'),
    url(r'^post/device/(?P<pk>\d+)/$', views.post_devicedetail, name='post_devicedetail'),
    url(r'^post/device/newDevice/$', views.post_devicenew, name='post_devicenew'),
    url(r'^post/device/(?P<pk>\d+)/edit/$', views.post_deviceedit, name='post_deviceedit'),

    url(r'^post/ajax_devicedetail', views.ajax_devicedetail, name='ajax_devicedetail'),
    url(r'^post/ajax_paddetail', views.ajax_paddetail, name='ajax_paddetail'),
    url(r'^post/ajax_chart_pad', views.ajax_chart_pad, name='ajax_chart_pad'),
]
