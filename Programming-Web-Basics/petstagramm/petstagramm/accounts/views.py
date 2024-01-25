from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
def signup_user(request):
    context = {}
    return render(request, template_name="accounts/signup_user.html", context=context)


def signin_user(request):
    context = {}
    return render(request, template_name="accounts/signin_user.html", context=context)


def signout_user(request):
    None


def details_profile(request, pk):
    context = {}
    return render(request, template_name="accounts/details_profile.html", context=context)

def signout_user(request):
    return redirect('index')

def edit_profile(request, pk):
    context = {}
    return render(request, template_name="accounts/edit_profile.html", context=context)


def delete_profile(request, pk):
    context = {}
    return render(request, template_name="accounts/delete_profile.html", context=context)