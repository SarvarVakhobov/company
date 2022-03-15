from unicodedata import category
from .forms import *
from django.contrib import admin
from .models import Category, Blog, Comments
from ckeditor.widgets import CKEditorWidget

# Register your models here.
admin.site.register(Category)
admin.site.register(Comments)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'date']
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Blog
        fields = '__all__'