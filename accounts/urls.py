from django.urls import path
from . import views

urlpatterns = [
    path('company_register', views.company_register, name="company_register"),
    path('worker_register', views.worker_register, name="worker_register"),
    path('com_login', views.com_login, name="com_login"),
    path('work_login', views.work_login, name="work_login"),
    path('user_logout', views.user_logout, name="user_logout"),
    path('user/<str:username>/', views.com_profile, name="com_profile"),
    path('addblog/<str:username>/', views.addblog, name="addblog"),
    path('editblog/<int:pk>/', views.editblog, name="editblog"),
    path('delete/<int:pk>/', views.delete_blog, name="delete_blog"),
    path('addpost/<str:username>/', views.addpost, name="addpost"),
    path('editpost/<int:pk>/', views.editpost, name="editpost"),
    path('delete/<int:pk>/', views.delete_post, name="delete_post"),
]
