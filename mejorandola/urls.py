from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
	url(r'^%s$' % settings.URL_PREFIX, 		   'website.views.home'), # home
	url(r'^%svideos/?$' % settings.URL_PREFIX, 'website.views.videos'), # archivo de videos
	url(r'^%svideo/(?P<video_slug>.+?)/?$' % settings.URL_PREFIX, 'website.views.video'), # video individual
    url(r'^%slive/?$' % settings.URL_PREFIX,   'website.views.live'),  # transmision en vivo

    url(r'^%supdate/?$' % settings.URL_PREFIX, 'github.views.update'), # actualizar el codigo
    url(r'^%sadmin/' % settings.URL_PREFIX, include(admin.site.urls)),
)
