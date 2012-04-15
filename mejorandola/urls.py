from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.contrib import admin
from feeds import VideoFeed

admin.autodiscover()

handler404 = 'website.views.handler404'

urlpatterns = patterns('',
	url(r'^$', 		   'website.views.home'), # home
	url(r'^videos/?$', 'website.views.videos'), # archivo de videos
	url(r'^videos/(?P<video_slug>.+?)/?$', 'website.views.video'), # video individual
    url(r'^live/?$',   'website.views.live'),  # transmision en vivo

    url(r'^feed/?$', VideoFeed(), name='feed'), # feed de videos
    url(r'^regenerate/?$', 'website.views.regenerate'),

    url(r'^update/?$', 'github.views.update'), # actualizar el codigo

    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
	urlpatterns += patterns('', 
		url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
	)