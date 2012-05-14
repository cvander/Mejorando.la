from django.contrib.syndication.views import Feed
from website.models import Video


class VideoFeed(Feed):
<<<<<<< HEAD
	title 		= 'Mejorando.la'
	link 		= 'http://mejorando.la'
	description = 'un show en vivo de gente que crea Internet, todos los jueves a las 4pm GMT-5'
	description_template = 'feeds/video_description.html'
=======
    title = 'Mejorando la Web'
    link = 'http://mejorando.la'
    description = ('un show en vivo de gente que crea Internet, '
                   'todos los jueves a las 4pm GMT-5')
    description_template = 'feeds/video_description.html'
>>>>>>> d64512ace1eae5e250b4c5d370f90bb511049379

    def items(self):
        return Video.objects.all().order_by('-fecha')[:15]

    def item_title(self, item):
        return item.titulo
