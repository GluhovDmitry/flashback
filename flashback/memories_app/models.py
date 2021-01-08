from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Owner', blank = True, null = True)
	description =  models.TextField(max_length=70)
	comment = models.TextField()
	#longitude = models.CharField(max_length=10)
	#latitude = models.CharField(max_length=10)

