from django.conf.urls import patterns, include, url
from inventory import views

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.category_list, name='home'),
    url(r'^(?P<category>[a-zA-Z_]+)/$', views.sub_category_list, name='subs'),
    url(r'^(?P<category>[a-zA-Z_]+)/(?P<sub_category>[a-zA-Z_]+)/$', views.inv_item_list, name='items'),
    # url(r'^(?P<category>\S+)/a/$', views.inv_item_list, name='items'),
)
