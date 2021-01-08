from django.db import models

class Post(models.Model):
	description =  models.TextField(max_length=70)
	comment = models.TextField()
	#longitude = models.CharField(max_length=10)
	#latitude = models.CharField(max_length=10)

