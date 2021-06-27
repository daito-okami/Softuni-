from django.shortcuts import render, redirect

# Create your views here.

from dNotes.core.notes_utlils import get_notes
from dNotes.core.profile_utils import get_profile
from dNotes.notes.forms import AddNoteForm, EditNoteForm, DeleteNoteForm
from dNotes.notes.models import Notes


def home(request):
    profile = get_profile()
    if not profile:
        return redirect('create profile')

    notes = Notes.objects.all()
    note = get_notes()
    context = {
        'note': note,
        'notes': notes
    }

    return render(request, 'home-with-profile.html', context)


def add_note(request):
    if request.method == 'POST':
        form = AddNoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddNoteForm()
    context = {
        'form': form
    }

    return render(request, 'note-create.html', context)


def edit_note(request, pk):
    note = Notes.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditNoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EditNoteForm(instance=note)
    context = {
        'note': note,
        'form': form
    }

    return render(request, 'note-edit.html', context)


def delete_note(request, pk):
    note = Notes.objects.get(pk=pk)
    if request.method == 'POST':
        note.delete()
        return redirect('home')
    else:
        form = DeleteNoteForm(instance=note)
    context = {
        'note': note,
        'form': form
    }

    return render(request, 'note-delete.html', context)


def details_note(request, pk):
    note = Notes.objects.get(pk=pk)

    context = {
        'note': note,
    }

    return render(request, 'note-details.html', context)