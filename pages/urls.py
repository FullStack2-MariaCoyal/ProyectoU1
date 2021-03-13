from django.urls import path
from .views import Home, Faqs, Contact

urlpatterns = [
    path('', Home.as_view(),               name='home'),
    path('faqs/', Faqs.as_view(),         name = 'faqs'),
    path('contact/', Contact.as_view(),     name = 'contact')
]