from unicodedata import category
from django.contrib import admin
from .models import Category, Blog, Comments

# Register your models here.
admin.site.register(Category)
admin.site.register(Comments)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'date']
