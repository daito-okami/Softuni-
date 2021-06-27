from django.shortcuts import render, redirect

# Create your views here.
from dNotes.core.notes_utlils import get_notes
from dNotes.core.profile_utils import get_profile
from dNotes.notes.models import Notes
from dNotes.profiles.forms import ProfileForm


def profile_info(request):
    profile = get_profile()
    all_notes = len(Notes.objects.all())

    context = {
        'profile': profile,
        'all_notes': all_notes
    }

    return render(request, 'profile.html', context)


def create_profile(request):
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProfileForm()

    context = {
        'form': form
    }

    return render(request, 'home-no-profile.html', context)





def delete_profile(request):
    profile = get_profile()
    profile.delete()
    Notes.objects.all().delete()
    return redirect('home')

    # context = {
    #
    # }
    #
    # return render(request, 'home-with-profile.html', context)