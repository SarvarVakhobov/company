from django.urls import path
from .views import blog, blogsingle

urlpatterns = [
    path('', blog, name='blog'),
    path('<int:pk>/', blogsingle, name='blogsingle')
]
