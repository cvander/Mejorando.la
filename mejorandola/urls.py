from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.contrib import admin
from feeds import VideoFeed

admin.autodiscover()

handler404 = 'website.views.handler404'

urlpatterns = patterns('',
    # home
    url(r'^$', 'website.views.home'),
    # archivo de videos
    url(r'^videos/?$', 'website.views.videos'),
    # video individual
    url(r'^videos/(?P<video_slug>.+?)/?$', 'website.views.video'),
    # transmision en vivo
    url(r'^live/?$', 'website.views.live'),
    # feed de videos
    url(r'^feed/?$', VideoFeed(), name='feed'),
    url(r'^regenerate/?$', 'website.views.regenerate'),
    # actualizar el codigo
    url(r'^update/?$', 'github.views.update'),

    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
    )
