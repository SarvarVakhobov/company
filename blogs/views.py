from re import search
from unicodedata import category
from django.shortcuts import redirect, render, HttpResponseRedirect
from django.db.models import Q

from .forms import BlogForm, CommentsForm
from .models import Blog, Category, Comments
from django.core.paginator import Paginator

from posts.models import Tag, Post

# Create your views here.
def blog(request):
    search_query = request.GET.get('search', '')

    CATID = request.GET.get('categories')

    if search_query:
        blogs = Blog.objects.filter(Q(title__icontains=search_query) | Q(text__icontains=search_query)).order_by('-date_time')
    elif CATID:
        blogs = Blog.objects.filter(category=CATID).order_by('-date_time')
    else:
        blogs = Blog.objects.all().order_by('-date_time')


    categories = Category.objects.all()
    tags = Tag.objects.all()
    paginator = Paginator(blogs, 2)
    page_number = request.GET.get('page')
    blog_obj = paginator.get_page(page_number)
    posts = Post.objects.all().order_by('-date_time')[:5]
    context = {
        'blog':blog_obj,
        'categories':categories,
        'tags':tags,
        'posts':posts,
        
    }

    return render(request, 'blog.html', context)

def blogsingle(request, pk):
    search_query = request.GET.get('search', '')
    if search_query:
        return redirect(f'../?search={search_query}')
    categories = Category.objects.all()
    blog = Blog.objects.get(id=pk)
    posts = Post.objects.all().order_by('-date_time')[:5]
    comment = Comments.objects.filter(blog=blog).order_by('-time')
    tags = Tag.objects.all()
    form = CommentsForm(request.POST)
    if request.POST:
        form = CommentsForm(request.POST)
        if form.is_valid():
            parent_obj = None
            try:
                parent_id = int(request.POST.get('parent_id'))
            except:
                parent_id = None
            if parent_id:
                parent_obj = Comments.objects.get(id=parent_id)
                if parent_obj:
                    replay_comment = form.save(commit=False)
                    replay_comment.parent = parent_obj
            new_com = form.save(commit=False)
            new_com.author = request.user
            new_com.blog = blog
            new_com.save()


    context = {
        'blog':blog,
        'categories':categories,
        'posts':posts,
        'tags':tags,
        'comment':comment,
        'form':form,
    }

    return render(request, 'blog-single.html', context)
