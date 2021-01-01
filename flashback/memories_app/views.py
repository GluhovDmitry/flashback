from django.shortcuts import render
from django.http import HttpResponse

#def description(request):
#	return HttpResponse("This service is managed to keep your memories...")

def description(request):
	return render(request, 'index.html', {})
