from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),

    url(r'^post/device/$', views.post_devicelist, name='post_devicelist'),
    url(r'^post/device/(?P<pk>\d+)/$', views.post_devicedetail, name='post_devicedetail'),
    url(r'^post/device/newDevice/$', views.post_devicenew, name='post_devicenew'),
    url(r'^post/device/(?P<pk>\d+)/edit/$', views.post_deviceedit, name='post_deviceedit'),

]
