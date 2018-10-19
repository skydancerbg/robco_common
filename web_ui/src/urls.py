from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'webui.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^interface/', include('interface.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('interface.urls')),
)
