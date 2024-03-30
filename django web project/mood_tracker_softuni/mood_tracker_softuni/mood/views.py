from django.contrib import auth
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from mood_tracker_softuni.mood.forms import RegisterForm, PostForm
from django.contrib.auth import login, logout, authenticate

from mood_tracker_softuni.mood.models import Post


# Create your views here.
@login_required(login_url="/login")
def home(request):
    posts = Post.objects.all()
    if request.method == "POST":
        post_id = request.POST.get("post-id")
        post = Post.objects.filter(id=post_id).first()
        if post and post.author == request.user:
            post.delete()
    return render(request, 'main/home.html', {'posts':posts})


@login_required(login_url="/login")
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("/home")
    else:
        form = PostForm()

    return render(request, 'main/create_post.html', {"form": form})
def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home')
    else:
        form = RegisterForm()

    return render(request, 'registration/sign-up.html', {'form': form})

def about_us(request):
    return render(request, 'main/about-us.html',)

def logout(request):
    auth.logout(request)
    return redirect('/home')