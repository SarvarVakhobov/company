from django import forms
from django.contrib import admin
from .models import Blog, Comments


class BlogForm(forms.ModelForm):
    class Meta(forms.ModelForm):
        model = Blog
        fields = ['title', 'text', 'category', 'image']

class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['message',]
