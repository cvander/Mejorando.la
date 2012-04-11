from django.contrib import admin
from models import Video, VideoComentario, Setting
from django.conf import settings

class VideoAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('titulo',)}
	ordering = ('-fecha',)

	class Media:
		js = ('http://ajax.googleapis.com/ajax/libs/jquery/1.7/jquery.min.js', 
			'%swymeditor/jquery.wymeditor.min.js' % settings.STATIC_URL, 
			'%sjs/admin.js' % settings.STATIC_URL
		)

class VideoComentarioAdmin(admin.ModelAdmin):
	ordering = ('-fecha',)
	readonly_fields = ('autor', 'autor_email','autor_url', 'content', 'video')

# registrar los modelos que utilizaran la interfaz de administracion d Django 
admin.site.register(Video, VideoAdmin)
admin.site.register(VideoComentario, VideoComentarioAdmin)
admin.site.register(Setting)