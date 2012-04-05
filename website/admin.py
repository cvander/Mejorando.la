from django.contrib import admin
from models import Video, Setting

class VideoAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('titulo',)}
	ordering = ('-fecha',)

# registrar los modelos que utilizaran la interfaz de administracion d Django 
admin.site.register(Video, VideoAdmin)
admin.site.register(Setting)