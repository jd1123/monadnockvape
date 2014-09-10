from django.conf.urls import patterns, url
from blog import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='blogindex'),
                       url(r'^(\d+)/$', views.index, name='blogindex'),
                       url(r'^post/$', views.blogpost, name='blogpost'),
                       url(r'^edit/(\d+)/$', views.blogpost, name='blogedit'),
                       url(r'^view/(\d+)/$', views.viewblogpost, name='blogview'),
                       )

