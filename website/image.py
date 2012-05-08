from django.conf import settings
import Image
import os

# constantes
THUMB = 'thumb'
SINGLE = 'single'
HOME = 'home'


# devolver la url a la imagen
def get_url_by(type, imagen):
    parts = str(imagen).rsplit('.', 1)
    return '%s%s-%s.%s' % (settings.MEDIA_URL, parts[0], type, parts[1])


# devolver el archivo a la imagen
def get_path_by(type, path):
    parts = path.rsplit('.', 1)
    return '%s-%s.%s' % (parts[0], type, parts[1])


def resize(type, imagen):
    path = os.path.join(settings.MEDIA_ROOT, str(imagen))

    # tomar el tamano del archivo de configuracion
    size = settings.IMG_SIZE_THUMB
    if type == SINGLE:
        size = settings.IMG_SIZE_SINGLE
    elif type == HOME:
        size = settings.IMG_SIZE_HOME

    try:
        image = Image.open(path)

        # sizes
        (width, height) = image.size
        (newWidth, newHeight) = size

        # relacion size actual, size nuevo
        ratioW = float(width) / newWidth
        ratioH = float(height) / newHeight
        ratio = ratioW if ratioW < ratioH else ratioH

        cropH, cropW = int(newHeight * ratio), int(newWidth * ratio)

        offsetX = (width - cropW) / 2
        offsetY = (height - cropH) / 2

        box = (offsetX, offsetY, cropW + offsetX, cropH + offsetY)
        image = image.crop(box)
        image = image.resize((newWidth, newHeight), Image.ANTIALIAS)

        # convertir a escala de grises
        if type == SINGLE:
            image = image.convert('L')

        # guardar la imagen
        image.save(get_path_by(type, path))
    except:
        pass
