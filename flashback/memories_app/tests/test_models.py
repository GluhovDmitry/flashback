from django.test import TestCase, Client, RequestFactory
from django.contrib.auth.models import User
from memories_app.models import *
from memories_app.forms import *
from django.urls import reverse


class TestModels(TestCase):
	def setUp(self):
		self.client = Client()
		self.test_user = User.objects.create(username='test_user')
		self.test_user.set_password('pword')
		self.test_user.save()
		self.test_memory = Post.objects.create(description='test_description', comment ='test_comment', lat=55.04, lng = 59.04)
		login = self.client.login(username='test_user', password='pword')
	def test_get_home(self):
		response = self.client.get(reverse('home'))
		self.assertEqual(response.status_code, 200)
	def test_get_form(self):
		response = self.client.get(reverse('memory'))
		self.assertEqual(response.status_code, 200)
	def test_get_item_from_memory(self):
		response = self.client.get('/memory/'+str(self.test_memory.id)+'/')
		self.assertEqual(response.context['post'].description, self.test_memory.description)
		self.assertEqual(response.status_code, 200)
	def test_post_item_to_form(self):
		response = self.client.post(
			reverse('memory'), 
			{'description':'desc_test',
			'comment':'comment_test',
			'lat':30.0,
			'lng':20.0
			})
		self.assertEquals(response.status_code, 302)
		self.assertEquals(Post.objects.count(), 2)
		self.assertEquals(Post.objects.get(pk=2).description, 'desc_test')
			
