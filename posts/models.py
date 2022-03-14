
from django.db import models
from accounts.models import Custom_user, Workers

class Tag(models.Model):
    tag = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self) -> str:
        return self.tag

class Post(models.Model):
    author = models.ForeignKey(Custom_user, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=300, blank=True)
    text = models.TextField()
    image = models.ImageField(upload_to="post/images")
    date = models.DateField(auto_now_add=True)
    date_time = models.DateTimeField(auto_now_add=True)
    tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self) -> str:
        return self.title

    







