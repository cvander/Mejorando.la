# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from models import Setting, Video, VideoComentario, VideoComentarioForm
from django.forms.models import model_to_dict
import GeoIP

# La vista del home muestra el ultimo video destacado
# y 4 videos mas, + el horario localizado
def home(solicitud):
	# checar si estamos transmitiendo en vivo
	# regresar la vista de "vivo" de ser asi
	if ('live' in solicitud.GET and solicitud.GET['live'] == '1') or Setting.objects.get(key='en_vivo').value:
		return render_to_response('website/live.html')

	# plantilla
	return render_to_response('website/home.html', {
		'ultimo_video': Video.objects.latest('fecha'), # el ultimo video
		'videos'	  : Video.objects.all()[1:5], # ultimos 4 videos
		'horario'	  : get_horario(solicitud.META['REMOTE_ADDR']), # el horario del programa localizado
	})

# el archivo muestra todos los videos 
# organizados por mes-año
def videos(solicitud):
	return render_to_response('website/videos.html', {
		'meses': [{
			'fecha' : fecha,
			'videos': Video.objects.filter(fecha__year=fecha.year, fecha__month=fecha.month)
		} for fecha in Video.objects.dates('fecha', 'month', order='DESC')]
	})

# la entrada de video muestra el video
# del capitulo + comentarios + formulario de comentarios
# tambien procesa +1 comentario
def video(solicitud, video_slug):
	# video por slug (nombre)
	video = Video.objects.get(slug=video_slug)
	
	# si son datos del formulario de comentarios
	if solicitud.method == 'POST':
		form = VideoComentarioForm(solicitud.POST)

		# validar los datos
		if(form.is_valid()):
			# asignar el video y guardar
			comentario = form.save(commit=False)
			comentario.video = video
			comentario.save()
	else:
		form = VideoComentarioForm()

	return render_to_response('website/video.html', {
		'video'		 : video, # datos del video particular
		'form'		 : form, # formulario de comentarios
		'comentarios': VideoComentario.objects.filter(video_id=video.id).order_by('-fecha', '-id') # comentarios al video
	})

# plantilla de transmision en vivo
def live(solicitud):
	return render_to_response('website/live.html')

# devuelve el horario del programa
# localizado por pais gracias a la 
# libreria GeoIP
def get_horario(ip):
	horario = {
		'pais': 'Centroamérica',
		'hora': '3pm'
	}

	geo = GeoIP.new(GeoIP.GEOIP_MEMORY_CACHE)

	country = geo.country_code_by_addr(ip)

	if country:
		country = country.lower()

		if country == 'mx':
			horario['pais'] = 'México'
			horario['hora'] = '4pm'
		elif country == 've':
			horario['pais'] = 'Venezuela'
			horario['hora'] = '3:30pm'
		elif country == 'co':
			horario['pais'] = 'Colombia'
			horario['hora'] = '4pm'
		elif country == 'pe':
			horario['pais'] = 'Perú'
			horario['hora'] = '4pm'
		elif country == 'ec':
			horario['pais'] = 'Ecuador'
			horario['hora'] = '4pm'
		elif country == 'bo':
			horario['pais'] = 'Bolivia'
			horario['hora'] = '5pm'
		elif country == 'cl':
			horario['pais'] = 'Chile'
			horario['hora'] = '6pm'
		elif country == 'ar':
			horario['pais'] = 'Argentina'
			horario['hora'] = '6pm'
		elif country == 'py':
			horario['pais'] = 'Paraguay'
			horario['hora'] = '6pm'
		elif country == 'uy':
			horario['pais'] = 'Uruguay'
			horario['hora'] = '6pm'
		elif country == 'br':
			horario['pais'] = 'Brasil'
			horario['hora'] = '7pm'
		elif country == 'es':
			horario['pais'] = 'España'
			horario['hora'] = '11pm'
	
	return horario