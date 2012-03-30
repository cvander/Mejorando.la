# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response


def home(solicitud):
	return render_to_response('website/home.html', {
		'horario': {
			'pais': 'Centroamérica',
			'hora': '3pm'
		},
		'title': 'Mejorando la Web | un show en vivo de gente que crea Internet, todos los jueves a las 4pm GMT-5',
		'ultimo_video': {
			'titulo': 'Nuevo diseño de #mejorandola',
			'imagen': 'http://mejorando.la/wp-content/uploads/2012/03/adan1.jpg',
			'url':'nuevo-diseno-de-mejorandola',
			
		}
		})

def videos(solicitud):
	return render_to_response('website/videos.html', {})

def video(solicitud, video_slug):
	return render_to_response('website/video.html', {})
