from django.contrib import admin
from .models import Post, Tag

# Register your models here.
admin.site.register(Tag)

@admin.register(Post)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'date']
