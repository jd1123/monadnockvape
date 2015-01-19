from django.conf.urls import patterns, include, url
from juiceprogram import views

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.index, name='home'),
	url(r'^lookup/$', views.user_lookup, name='lookup'),
	url(r'^user/(\d+)/$', views.user_view, name='user'),
)
