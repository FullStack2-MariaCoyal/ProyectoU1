from django.shortcuts import render

# Create your views here.

from django.views.generic.base import TemplateView

class Home(TemplateView):
    template_name = 'home.html'

class Faqs(TemplateView):
    template_name = 'faqs.html'

class Contact(TemplateView):
    template_name = 'contact.html'