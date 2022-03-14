from multiprocessing import context
from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import Contactform

from accounts.models import Custom_user, Workers
from posts.models import Post, Tag

# Create your views here.
def home(request):
    company = Custom_user.objects.all().order_by('-date_modified')[:8]
    posts = Post.objects.all().order_by('-date_time')[:10]
    tags = Tag.objects.all()

    context = {
        'company':company,
        'posts':posts,
        'tags':tags,

    }

    return render(request, 'index.html', context)

def about(request):
    company = Custom_user.objects.all().order_by('-date_modified')[:8]
    context = {
        'company':company,
    }
    return render(request, 'about.html', context)

def contact(request):
    form = Contactform()
    if request.POST:
        form = Contactform(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()

    context = {
        'form':form,
    }
    return render(request, 'contact.html', context)

def services(request):
    return render(request=request, template_name='services.html')

def team(request):
    worker = Workers.objects.filter(company=request.user)

    context = {
        'worker':worker,
    }
    return render(request, 'team.html', context)
