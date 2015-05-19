from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'basefunctions.views.root', name='home'),
    url(r'^login/$', 'basefunctions.views.user_login', name = 'login'),
    url(r'^logout/$', 'basefunctions.views.user_logout', name = 'logout'),
    #url(r'^c/', include('inventory.urls')),
    url(r'^juiceprogram/', include('juiceprogram.urls')),
    # url(r'^blog/', include('blog.urls')),
    url(r'^login/$', 'basefunctions.views.user_login', name='login'),
    url(r'^logout/$', 'basefunctions.views.user_logout', name='logout'),
    url(r'^admin/', include(admin.site.urls)),
)
