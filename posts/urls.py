from django import views
from django.urls import path
from .views import *



urlpatterns = [
    path('post/',view=post, name='post'),
    path('post/<str:title>/',view=postdateils, name='postdateils'),
]
