from django.contrib import auth
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib import messages
from mood_tracking1.mood.forms import RegisterForm, PostForm
from django.contrib.auth import login, logout, authenticate

from mood_tracking1.mood.models import Post
from mood_tracking1.friends.models import Friend

# Create your views here.

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

@login_required
def account(request):
    friends = request.user.friends.all()
    return render(request, 'main/account.html', {'friends':friends})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        request.user.username = request.POST.get('username')
        request.user.email = request.POST.get('email')
        request.user.save()

        messages.info(request, 'The changes were saved')
        return redirect('account')

    return render(request, 'main/edit_profile.html')


@login_required
def dashboard(request):
    return render(request, 'main/dashboard.html',)
