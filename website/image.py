from django.conf import settings
import Image
import os

# constantes
THUMB   = 'thumb'
SINGLE  = 'single'
HOME    = 'home'

# devolver la url a la imagen
def get_url_by(type, imagen):
	parts = str(imagen).rsplit('.', 1)
	return '%s%s-%s.%s' % (settings.MEDIA_URL, parts[0], type, parts[1])

# devolver el archivo a la imagen
def get_path_by(type, path):
	parts = path.rsplit('.', 1)
	return '%s-%s.%s' % (parts[0], type, parts[1])

def resize(type, imagen):
	path  = os.path.join(settings.MEDIA_ROOT, str(imagen))

	# tomar el tamano del archivo de configuracion
	size = settings.IMG_SIZE_THUMB
	if type == SINGLE: size = settings.IMG_SIZE_SINGLE
	elif type == HOME: size = settings.IMG_SIZE_HOME

	try:
		image = Image.open(path)

		(width, height)       = image.size
		(newWidth, newHeight) = size

		# convertir los valores a float??
		width     = float(width)
		height    = float(height)
		newWidth  = float(newWidth)
		newHeight = float(newHeight)

		# calcular la relacion entre nuevos y viejos tamanos
		heightRatio = height / newHeight
		widthRatio  = width / newWidth

		# calcular la relacion total
		if heightRatio < widthRatio:
			optimalRatio = heightRatio
		else:
			optimalRatio = widthRatio

		# calcular los tamanos optimos para hacer el cambio
		optiomalHeight = height / optimalRatio
		optimalWidth   = width / optimalRatio

		# cambiar el tamano y recortar	
		image = image.resize((int(optimalWidth), int(optiomalHeight)), Image.ANTIALIAS)
		image = image.crop((0, 0, int(newWidth), int(newHeight)))

		# convertir a escala de grises
		if type == SINGLE: image = image.convert('L')

		# guardar la imagen
		image.save(get_path_by(type, path))
	except:
		pass