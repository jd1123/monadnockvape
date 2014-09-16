from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'basefunctions.views.root', name='home'),
    url(r'^about/$', 'basefunctions.views.about', name = 'about'),
    url(r'^contact/$', 'basefunctions.views.contact', name = 'contact'),
    url(r'^c/', include('inventory.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
