from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Owner', blank = True, null = True)
	description =  models.TextField(max_length=20)
	comment = models.TextField(max_length=50)
	lat = models.FloatField(max_length=10, default = 0.0, blank=True, null = True)
	lng = models.FloatField(max_length=10, default = 0.0, blank=True, null = True)
	
