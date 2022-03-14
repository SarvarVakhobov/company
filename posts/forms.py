from django import forms
from django.contrib import admin
from .models import Post

class PostForm(forms.ModelForm):
    class Meta(forms.ModelForm):
        model = Post
        fields = ['title', 'text', 'author', 'image', 'tag']
