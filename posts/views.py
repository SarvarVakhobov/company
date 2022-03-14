from multiprocessing import context
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Post, Tag


def post(request):

    TAGID = request.GET.get('tagid')
    if TAGID:
        posts = Post.objects.filter(tag=TAGID).order_by('-date_time')
    else:
        posts = Post.objects.all().order_by('-date_time')
    tags = Tag.objects.all()
    context = {
        'posts':posts,
        'tags':tags,
    }
    return render(request, 'post.html', context)

def postdateils(request, title):
    post = Post.objects.get(title=title)

    context = {
        'post':post,
    }

    return render(request, 'post-details.html', context)