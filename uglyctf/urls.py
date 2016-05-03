#coding:utf-8
from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(r'',
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('ctfweb.urls')),
)
