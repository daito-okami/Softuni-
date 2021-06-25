from django.shortcuts import render, redirect

# Create your views here.
from exam_prep.core.profile_utils import get_profile
from exam_prep.profiles.forms import CreateProfileForm, EditProfileForm


def profile_info(request):
    profile = get_profile()
    context = {
        'profile': profile
    }

    return render(request, 'profile.html', context)


def create_profile(request):
    if request.method == "POST":
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreateProfileForm()

    context = {
        'form': form,
    }

    return render(request, 'home-no-profile.html', context)


def profile_edit(request):
    profile = get_profile()
    if request.method == "POST":
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EditProfileForm(instance=profile)

    context = {
        'form': form,
    }

    return render(request, 'profile-edit.html', context)


def profile_delete(request):
    profile = get_profile()
    if request.method == "POST":
        profile.delete()
        return redirect('home')

    context = {

    }

    return render(request, 'profile-delete.html', context)