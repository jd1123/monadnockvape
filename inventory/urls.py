from django.conf.urls import patterns, include, url
from inventory import views

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.root, name='home'),
)
