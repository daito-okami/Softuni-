from django import forms

from dNotes.notes.models import Notes


class NoteForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = '__all__'


class AddNoteForm(NoteForm):
    pass


class EditNoteForm(NoteForm):
    pass


class DeleteNoteForm(NoteForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'