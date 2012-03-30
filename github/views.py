from django.http import HttpResponse

import commands

def update(solicitud):
	return HttpResponse(commands.getstatusoutput('git pull')[1])