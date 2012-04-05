from django.contrib import admin
from models import Video, VideoComentario, Setting

class VideoAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('titulo',)}
	ordering = ('-fecha',)

class VideoComentarioAdmin(admin.ModelAdmin):
	ordering = ('-fecha',)
	readonly_fields = ('autor', 'autor_email','autor_url', 'content', 'video')

# registrar los modelos que utilizaran la interfaz de administracion d Django 
admin.site.register(Video, VideoAdmin)
admin.site.register(VideoComentario, VideoComentarioAdmin)
admin.site.register(Setting)