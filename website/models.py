from django.db import models
from django.forms import ModelForm
from django.conf import settings

# para guardar opciones del sitio (aka switches)
class Setting(models.Model):
	value = models.CharField(max_length=100)
	key   = models.CharField(max_length=50)

# el archivo de videos
class Video(models.Model):
	titulo 		= models.CharField(max_length=150)
	slug	    = models.CharField(max_length=300)
	imagen 	    = models.ImageField(upload_to='static/videos')
	fecha 	    = models.DateField()
	embed_code  = models.TextField()
	descripcion = models.TextField()

	# el permalink
	def get_absolute_url(self):
		return '/%svideo/%s/' % (settings.URL_PREFIX, self.slug)
	# los diferentes imagenes para el sitio
	def get_home_image_url(self):
		return 'http://dev.mejorando.la/resizer.php?s=h&u=http://mejorando.la/wp-content/uploads/%s' % self.imagen

	def get_thumb_image_url(self):
		return 'http://dev.mejorando.la/resizer.php?s=t&u=http://mejorando.la/wp-content/uploads/%s' % self.imagen

	def get_single_image_url(self):
		return 'http://dev.mejorando.la/resizer.php?s=p&u=http://mejorando.la/wp-content/uploads/%s' % self.imagen

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


