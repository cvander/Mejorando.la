from django.http import HttpResponse
from django.conf import settings

import commands

# hace git pull y copia los archivos estaticos a public_html
def update(solicitud):
	gitpull = commands.getstatusoutput('git pull')[1]
	
	return HttpResponse(gitpull)