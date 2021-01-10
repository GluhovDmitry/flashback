from django.core import serializers
from .models import *

class MapSerializer(serializers.ModelSerializer):
	class Meta:
		model = Map
		fields = ['latitude', 'longitude']
