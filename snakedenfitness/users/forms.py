from django import forms
from django.contrib.auth.models import User
from .models import User, Profile, clientTrainer
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')


class ProfileForm(forms.ModelForm):
    bio = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Profile
        fields = ('birth_date', 'bio', 'role', 'avatar')

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        if not self.cleaned_data.get('avatar'):
            self.instance.avatar = 'generic-avatar.png'
        super().save(commit)