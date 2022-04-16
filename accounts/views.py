from django.contrib import messages
from django.http import Http404
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout

from .models import Custom_user, Workers
from .forms import Com_userForm, Com_editForm, WorkersForm, Worker_editForm

from blogs.forms import BlogForm
from blogs.models import Blog

from posts.forms import PostForm
from posts.models import Post

# Create your views here.
def company_register(request):
    form = Com_userForm(request.POST)
    if request.method == "POST":
        form = Com_userForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data.get('username')
            user = form.save(commit=False)
            user.save()
            return redirect('com_login')
        else:
            form = Custom_user()
            messages.error(request, "Not found")
    context = {
        'form':form,
    }         
    return render(request, 'login_reg/registercom.html', context)

def com_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('index')
        else:
            return redirect('com_login')

    return render(request, 'login_reg/logincom.html')

def user_logout(request):
    logout(request)
    return redirect('index')

def com_profile(request, username):
    try:
        user = Custom_user.objects.get(username=username)
    except Custom_user.DoesNotExist:
        return Http404
    worker = Workers.objects.filter(company=request.user)
    form = Com_editForm(request.POST or None, request.FILES or None, instance=user)
    if request.method == 'POST':
        form = Com_editForm(request.POST or None, request.FILES or None, instance=user)
        if form.is_valid():
            form.save()
            return redirect('com_profile', user.username)
    context = {
        'form':form,
        'user':user,
        'worker':worker,
    }
    return render(request, 'login_reg/profilecom.html', context)



def worker_register(request):
    form = WorkersForm(request.POST)
    if request.method == "POST":
        form = WorkersForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.company = request.user
            obj.save()
            return redirect('work_login')
        else:
            form = Workers()
            messages.error(request, "Not found")
    context = {
        'form':form,
    }         
    return render(request, 'login_reg/registerwork.html', context)

def work_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        try:
            worker = Workers.objects.get(username=username, password1=password1)
        except:
            return redirect('work_login')

        if worker.category_worker == "Bg":
            return redirect('addblog', request.user.username)
        if worker.category_worker == "Pt":
            return redirect('addpost', request.user.username)
        else:
            return redirect('com_profile', request.user.username)

    return render(request, 'login_reg/loginwork.html')

def addblog(request, username):
    blogs = Blog.objects.filter(author=request.user).order_by('-date_time')
    form = BlogForm()
    print('1')
    if request.POST:
        form = BlogForm(request.POST, request.FILES)
        print('2')
        if form.is_valid():
            print('3')
            obj = form.save(commit=False)
            obj.author = request.user
            obj.save()
            return redirect('addblog', request.user.username) 

    context = {
        'blogs':blogs,
        'form':form,
    }

    return render(request, 'login_reg/create_blog.html', context)

def editblog(request, pk):
    blog = Blog.objects.get(id=pk)
    form = BlogForm(request.POST or None, request.FILES or None, instance=blog)
    if request.method == 'POST':
        form = BlogForm(request.POST or None, request.FILES or None, instance=blog)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author = request.user
            obj.save()
            return redirect('addblog', request.user)
    context = {
        'form':form,
        'blog':blog,
    }
    return render(request, 'login_reg/edit_blog.html', context)

def delete_blog(request, pk):
    blog = Blog.objects.get(id=pk)
    blog.delete()
    return redirect('addblog', request.user)


def addpost(request, username):
    posts = Post.objects.filter(author=request.user).order_by('-date_time')
    form = PostForm()
    print('1')
    if request.POST:
        form = PostForm(request.POST, request.FILES)
        print('2')
        if form.is_valid():
            print('3')
            obj = form.save(commit=False)
            obj.author = request.user
            obj.save()
            return redirect('addpost', request.user.username) 

    context = {
        'posts':posts,
        'form':form,
    }

    return render(request, 'login_reg/create_post.html', context)

def editpost(request, pk):
    post = Post.objects.get(id=pk)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    if request.method == 'POST':
        form = PostForm(request.POST or None, request.FILES or None, instance=post)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author = request.user
            obj.save()
            return redirect('addpost', request.user)
    context = {
        'form':form,
        'post':post,
    }
    return render(request, 'login_reg/edit_post.html', context)

def delete_post(request, pk):
    blog = Post.objects.get(id=pk)
    blog.delete()
    return redirect('addpost', request.user)


