from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.contrib import admin
from feeds import VideoFeed

admin.autodiscover()

handler404 = 'website.views.handler404'

urlpatterns = patterns('',
<<<<<<< HEAD
	url(r'^$', 		   'website.views.home'), # home
    url(r'^cursos/?$', 'website.views.cursos'), # archivo de cursos
	url(r'^videos/?$', 'website.views.videos'), # archivo de videos
	url(r'^videos/(?P<video_slug>.+?)/?$', 'website.views.video'), # video individual
    url(r'^live/?$',   'website.views.live'),  # transmision en vivo

    url(r'^feed/?$', VideoFeed(), name='feed'), # feed de videos
=======
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
>>>>>>> d64512ace1eae5e250b4c5d370f90bb511049379
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
