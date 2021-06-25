from django import forms

from exam_prep.profiles.models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

class CreateProfileForm(ProfileForm):
    pass


class EditProfileForm(ProfileForm):
    pass