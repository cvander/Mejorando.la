from django.db import models
from django.forms import ModelForm
from django.conf import settings

# para guardar opciones del sitio (aka switches)
class Setting(models.Model):
	value = models.BooleanField(default=False)
	key   = models.CharField(max_length=50)

	def __unicode__(self):
		return self.key

# el archivo de videos
class Video(models.Model):
	titulo 		= models.CharField(max_length=150)
	slug	    = models.CharField(max_length=300)
	imagen 	    = models.ImageField(upload_to='media/videos')
	fecha 	    = models.DateField()
	embed_code  = models.TextField()
	descripcion = models.TextField()

	def __unicode__(self):
		return self.titulo

	# el permalink
	def get_absolute_url(self):
		return '/%svideo/%s/' % (settings.URL_PREFIX, self.slug)

	# los diferentes imagenes para el sitio
	def get_home_image_url(self):
		return 'http://dev.mejorando.la/resizer.php?s=h&u=%s' % settings.MEDIA_URL+str(self.imagen)

	def get_thumb_image_url(self):
		return 'http://dev.mejorando.la/resizer.php?s=t&u=%s' % settings.MEDIA_URL+str(self.imagen)

	def get_single_image_url(self):
		return 'http://dev.mejorando.la/resizer.php?s=p&u=%s' % settings.MEDIA_URL+str(self.imagen)

# comentarios de los videos
class VideoComentario(models.Model):
	autor_email = models.EmailField()
	autor_url   = models.URLField(blank=True)
	autor 		= models.CharField(max_length=150)
	fecha 		= models.DateField(auto_now_add=True)
	content 	= models.TextField()
	video 		= models.ForeignKey(Video)

# el formulario para agregar un comentario al video
class VideoComentarioForm(ModelForm):
	class Meta:
		model  = VideoComentario
		fields = ('autor', 'autor_email', 'autor_url', 'content')


