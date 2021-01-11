from django.test import TestCase, Client
from memories_app.views import *
from django.urls import reverse

class TestViews(TestCase):
	def setUp(self):
		self.client = Client()
	def test_unauthorized_links_access(self):
		urls_list = ['home', 'memory']
		for url in urls_list:
			response=self.client.get(reverse(url))
			self.assertEqual(response.status_code, 302)
		

