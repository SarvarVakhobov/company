from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Category_company(models.Model):
    category = models.CharField(max_length=300)

    def __str__(self):
        return self.category

class Custom_user(AbstractUser):
    name = models.CharField(max_length=200, blank=True)
    category_company = models.ForeignKey(Category_company, on_delete=models.CASCADE, blank=True, null=True)
    number = models.PositiveIntegerField(blank=True, null=True)
    bio = models.CharField(max_length=300, blank=True)
    email = models.EmailField(blank=True)
    avatar = models.ImageField(upload_to = 'images/company', blank=True, default= '../static/images/com_avatar1.jpg', null=True)
    telegram_link = models.URLField(blank=True)
    facebook_link = models.URLField(blank=True)
    instagram_link = models.URLField(blank=True)
    date_published = models.DateField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

    @property
    def get_avatar(self):
        if self.avatar and hasattr(self.avatar, 'url'):
            return self.avatar.url
        else:
            return "../static/images/com_avatar.jpg"


class Workers(models.Model):
    GENDER = (
        ('',''),
        ('ERKAK','ERKAK'),
        ('AYOL','AYOL'),
    )
    CATEGORY = (
        ('An', 'Admin'),
        ('Pt', 'Post admin'),
        ('Bg', 'Blog admin'),

    )
    username = models.CharField(max_length=100, blank=True)
    password1 = models.CharField(max_length=50, blank = True)
    password2 = models.CharField(max_length=50, blank = True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=True, null=True)
    number = models.PositiveIntegerField(blank=True, null=True)
    company = models.ForeignKey(Custom_user, blank=True, on_delete=models.CASCADE, null=True)
    category_worker = models.CharField(max_length=10, choices=CATEGORY, null=True, blank=True)
    avatar = models.ImageField(upload_to = 'images/workers/', blank=True, default= '../static/images/avatar.jpg', null=True)
    gender = models.CharField(max_length=10, choices=GENDER, default='', blank=True)

    @property
    def get_avatar(self):
        if self.avatar and hasattr(self.avatar, 'url'):
            return self.avatar.url
        else:
            return "../static/images/avatar.jpg"

    def save(self, *args, **kwargs):
        if self.password1==self.password2:
            return super().save(*args, **kwargs)

        
