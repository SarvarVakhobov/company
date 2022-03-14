from django.db import models
from accounts.models import Custom_user, Workers

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self) -> str:
        return self.category

    def get_count(self):
        return self.blog.count()


class Blog(models.Model):
    author = models.ForeignKey(Custom_user, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=300, blank=True)
    text = models.TextField()
    image = models.ImageField(upload_to="blog/images")
    date = models.DateField(auto_now_add=True)
    date_time = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, related_name='blog', on_delete=models.SET_NULL, blank=True, null=True)
    # tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self) -> str:
        return self.title

    def get_comment_count(self):
        return self.comments.count()


class Comments(models.Model):
    message = models.TextField()
    author = models.ForeignKey(Custom_user, related_name='comments', on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)


    def __str__(self):
        return '%s - %s' % (self.author.username, self.blog.title)





