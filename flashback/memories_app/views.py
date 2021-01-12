from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from django.shortcuts import redirect
from .models import Post
from django.views.generic.list import ListView


def privacy_policy(request):
	return render(request, 'privacy_policy.html', {})
def login(request):
	return render(request, 'login.html', {})
@login_required
def home(request):
	posts = Post.objects.all()
	return render(request, 'home.html', {'posts' : posts})
	
@login_required	
def memory(request):
	mapbox_token = 'pk.eyJ1IjoiZGRkaW1hIiwiYSI6ImNram40dWo2NzJqcDkyeWxvZTNhbGxmc2UifQ.dtshxzx_TGEO_hl_1iN-7Q'
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.lng = float(request.POST.get('lng'))
			post.lat = float(request.POST.get('lat'))
			post.save()
			return redirect('memory_detail', pk=post.pk)
	else: form = PostForm()
	return render(request, 'memory.html', {'mapbox_token' : mapbox_token, 'form' : form})
@login_required
def memory_detail(request, pk):
	mapbox_token = 'pk.eyJ1IjoiZGRkaW1hIiwiYSI6ImNram40dWo2NzJqcDkyeWxvZTNhbGxmc2UifQ.dtshxzx_TGEO_hl_1iN-7Q'
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'memory_detail.html', {'mapbox_token' : mapbox_token, 'post': post})

