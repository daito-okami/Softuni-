from dNotes.notes.models import Notes



def get_notes():
    return Notes.objects.first()