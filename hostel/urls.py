from django.conf.urls import url
from django.urls import path
from . import views
app_name = 'hostel'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    path(r'^register/$', views.register, name='register'),
    path(r'^student_details/$', views.student_details, name='student_details'),
    path(r'^login/$', views.user_login, name='login'),
    path(r'^logout/$', views.logout1, name='logout'),
    path(r'^change/$', views.changereq, name='change_req'),
    path(r'^swap/$', views.swap, name='swap_req'),
    path(r'^ack/$', views.ack, name='swap_ack'),
    path(r'^allocate/$', views.allocate, name='allocate'),
    path(r'^success/$', views.success, name='success'),
    path(r'^adminchange/$', views.adminchange, name='change'),
    path(r'^adminswap/$', views.adminswap, name='swap'),
    path(r'^deallocate/$', views.deallocate, name='deallocate'),
    path(r'^allrequest/$', views.allrequest, name='request'),
    path(r'^vacant/$', views.vacant, name='vacant'),
    path(r'^student/$', views.allstudent, name='student'),
]