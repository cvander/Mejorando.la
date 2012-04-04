from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 		   'website.views.home'), # home
	url(r'^videos/?$', 'website.views.videos'), # archivo de videos
	url(r'^video/(?P<video_slug>.+?)/?$', 'website.views.video'), # video individual
    url(r'^live/?$',   'website.views.live'),  # transmision en vivo

    url(r'^update/?$', 'github.views.update'), # actualizar el codigo
    url(r'^admin/', include(admin.site.urls)),
)
