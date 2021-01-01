from django.shortcuts import render
from django.http import HttpResponse

#def description(request):
#	return HttpResponse("This service is managed to keep your memories...")

def index(request):
	return render(request, 'index.html', {})
@login_required
def home(request):
	return render(request, 'home.html', {})

def login(request):
	return render(request, 'login.html', {})
