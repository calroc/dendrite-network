from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin


admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$', 'dendnet.views.home', name='home'),
    url(r'^describe/?$', 'dendnet.views.describe', name='describe'),
    url(r'^d3demo/?$', 'dendnet.views.d3demo', name='d3demo'),
    url(r'^register/?$', 'dendnet.views.register', name='register'),
    url(
        r'^bump'
        r'/(?P<me>[a-zA-Z0-9]{32})'
        r'/(?P<it>[a-zA-Z0-9]{32})'
        r'/(?P<you>[a-zA-Z0-9]{32})$',
        'dendnet.views.bump',
        name='bump'
        ),
    url(
        r'^engage'
        r'/(?P<me>[a-zA-Z0-9]{32})'
        r'/(?P<it>[a-zA-Z0-9]{32})',
        'dendnet.views.engage',
        name='engage'
        ),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^static/(?P<path>.*)$',
        'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT},
        ),
)
