from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
#from .views import ThingList, ThingCreate, ThingDetail, ThingUpdate, ThingDelete
from . import views

urlpatterns = [
    url(r'^javaTutor/demo1/$', views.javatutor_demo1, name='demo1'),
    url(r'^javaTutor/demo2/$', views.javatutor_demo2, name='demo2'),
    url(r'^javaTutor/demo3/$', views.javatutor_demo3, name='demo3'),
    url(r'^javaTutor/demo4/$', views.javatutor_demo4, name='demo4'),
    url(r'^javaTutor/demo5/$', views.javatutor_demo5, name='demo5'),
    url(r'^javaTutor/demo21/$', views.javatutor_demo21, name='demo21'),
    url(r'^javaTutor/demo22/$', views.javatutor_demo22, name='demo22'),
    url(r'^javaTutor/demo23/$', views.javatutor_demo23, name='demo23'),
    url(r'^javaTutor/demo24/$', views.javatutor_demo24, name='demo24'),
    url(r'^javaTutor/demo25/$', views.javatutor_demo25, name='demo25'),
    url(r'^javaTutor/demo26/$', views.javatutor_demo26, name='demo26'),
    url(r'^javaTutor/demo27/$', views.javatutor_demo27, name='demo27'),
    url(r'^javaTutor/demo28/$', views.javatutor_demo28, name='demo28'),
    url(r'^javaTutor/demo31/$', views.javatutor_demo31, name='demo31'),
    url(r'^javaTutor/demo32/$', views.javatutor_demo32, name='demo32'),
    url(r'^javaTutor/demo33/$', views.javatutor_demo33, name='demo33'),
    url(r'^javaTutor/demo34/$', views.javatutor_demo34, name='demo34'),
    url(r'^javaTutor/demo41/$', views.javatutor_demo41, name='demo41'),
    url(r'^javaTutor/demo42/$', views.javatutor_demo42, name='demo42'),
    url(r'^javaTutor/demo43/$', views.javatutor_demo43, name='demo43'),
    url(r'^javaTutor/demo44/$', views.javatutor_demo44, name='demo44'),
    url(r'^javaTutor/demo45/$', views.javatutor_demo45, name='demo45'),
    url(r'^javaTutor/demo46/$', views.javatutor_demo46, name='demo46'),
    url(r'^javaTutor/demo47/$', views.javatutor_demo47, name='demo47'),
    url(r'^javaTutor/demo51/$', views.javatutor_demo51, name='demo51'),
    url(r'^javaTutor/demo52/$', views.javatutor_demo52, name='demo52'),
    url(r'^javaTutor/demo53/$', views.javatutor_demo53, name='demo53'),
    url(r'^javaTutor/demo54/$', views.javatutor_demo54, name='demo54'),
    url(r'^javaTutor/demo55/$', views.javatutor_demo55, name='demo55'),
    url(r'^javaTutor/demo56/$', views.javatutor_demo56, name='demo56'),
    url(r'^javaTutor/demo57/$', views.javatutor_demo57, name='demo57'),

    url(r'^javaTutor/DragDrop1/$', views.javatutor_DragDrop1, name='DragDrop1'),

    url(r'^javaTutor/demo61/$', views.javatutor_demo61, name='demo61'),
    url(r'^javaTutor/demo62/$', views.javatutor_demo62, name='demo62'),
    url(r'^javaTutor/demo63/$', views.javatutor_demo63, name='demo63'),
    url(r'^javaTutor/git_anywhere/$', views.javatutor_git_anywhere, name='git_anywhere'),

    url(r'^ajx/mygetview', views.mygetview, name='mygetview'),
    url(r'^ajx/mypostview', views.mypostview, name='mypostview'),
    url(r'^ajx/myajaxview', views.myajaxview, name='myajaxview'),
    url(r'^ajx/myajaxformview', views.myajaxformview, name='myajaxformview'),

] + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)