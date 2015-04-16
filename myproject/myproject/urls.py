from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^urls/$', "acortador.views.all"),
    url(r'^urls/(.*$)', "acortador.views.url"),
    url(r'^(.*$)', "acortador.views.notfound"),
)
