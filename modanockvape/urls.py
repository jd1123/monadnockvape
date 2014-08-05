from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'basefunctions.views.root', name='home'),
    url(r'^i/$', include('inventory.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
