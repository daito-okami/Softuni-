from django import forms

from mood_tracking1.mood_tracked.models import Activity


class ActivityForm(forms.ModelForm):
    mood = forms.ChoiceField(choices=Activity.MOOD_CHOICES)  # Explicitly use ChoiceField

    class Meta:
        model = Activity
        fields = ['tasks', 'title', 'mood']