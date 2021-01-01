from django.shortcuts import render
from django.http import HttpResponse

def description(request):
	return HttpResponse("This service is managed to keep your memories...")


