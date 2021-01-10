from django.db import models
from django.contrib.auth.models import User
from jsonfield import JSONField
#from geoposition.fields import GeopositionField
class Post(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Owner', blank = True, null = True)
	description =  models.TextField(max_length=20)
	comment = models.TextField(max_length=50)
	#position = GeopositionField(default='')
	#lngLat = JSONField(default = '', blank=True, null = True)
	lat = models.FloatField(max_length=10, default = 0.0, blank=True, null = True)
	lng = models.FloatField(max_length=10, default = 0.0, blank=True, null = True)
	
