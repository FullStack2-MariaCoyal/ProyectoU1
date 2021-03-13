from django.test import TestCase

# Create your tests here.
from django.test import SimpleTestCase
from django.urls import reverse
# Create your tests here.
class STC(SimpleTestCase): 
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status.code, 200)
    def test_about_page_status_code(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status.code, 200)