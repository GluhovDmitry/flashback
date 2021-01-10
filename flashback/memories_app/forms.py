from django import forms
#from jsonfield.fields import JSONFormField
from .models import Post
#from splitjson.widgets import SplitJSONWidget

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('description',
			  'comment',)
		
