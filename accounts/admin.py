from django.contrib import admin
from .models import Custom_user, Category_company, Workers

# Register your models here.
@admin.register(Custom_user)
class UserAdmin(admin.ModelAdmin):
    list_display  = ['id','username', 'name', 'category_company']
    list_diplay_links = ('id','username', 'name', 'category_company')

@admin.register(Workers)
class WorkersAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'company', 'category_worker']
    list_display_links = ('id', 'username')

admin.site.register(Category_company)
