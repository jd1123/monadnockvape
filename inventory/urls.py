from django.conf.urls import patterns, include, url
from inventory import views

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.category_page, name='home'),
    url(r'^(?P<category>\S+)/$', views.sub_category_page, name='subs'),
)
