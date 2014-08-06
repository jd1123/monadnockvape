from django.conf.urls import patterns, include, url
from inventory import views

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.category_list, name='home'),
    url(r'^(?P<category>\S+)/$', views.sub_category_list, name='subs'),
    url(r'^(?P<category>\S+)/(?P<sub_category>\S+)/$', views.inv_item_list, name='items')
)
