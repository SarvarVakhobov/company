from django import views
from django.urls import path
from .views import *



urlpatterns = [
    path('', view=home, name='index'),
    path('about/',view=about, name='about'),
    path('contact/',view=contact, name='contact'),
    path('services/',view=services, name='services'),
    path('team/',view=team, name='team'),
]
