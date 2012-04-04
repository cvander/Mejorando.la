from django.contrib import admin
from models import Video, Setting

# registrar los modelos que utilizaran la interfaz de administracion d Django 
admin.site.register(Video)
admin.site.register(Setting)