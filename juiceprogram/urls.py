from django.conf.urls import patterns, include, url
from juiceprogram import views

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.index, name='home'),
	url(r'^create/$', views.create, name='create'),
	url(r'^lookup/$', views.user_lookup, name='lookup'),
	url(r'^user/(\d+)/$', views.user_view, name='user'),
	url(r'^user_list/(\d+)/$', views.user_list, name='user_list'),
	url(r'^alphabetic_list/([A-Z])/$', views.alphabetic_list, name='alphabetic_list'),
)
