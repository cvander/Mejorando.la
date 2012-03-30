from django.http import HttpResponse
from django.conf import settings

import commands

def update(solicitud):
	gitpull = commands.getstatusoutput('git pull')[1]
	commands.getstatusoutput('cp -R static/* %s' % settings.HTTPD_STATIC)[1]
	return HttpResponse(gitpull)