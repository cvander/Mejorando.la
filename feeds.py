from django.contrib.syndication.views import Feed
from website.models import Video

class VideoFeed(Feed):
	title 		= 'Mejorando la Web'
	link 		= 'http://mejorando.la'
	description = 'un show en vivo de gente que crea Internet, todos los jueves a las 4pm GMT-5'

	def items(self):
		return Video.objects.all()[:15]

	def item_title(self, item):
		return item.titulo

	def item_description(self, item):
		return item.descripcion