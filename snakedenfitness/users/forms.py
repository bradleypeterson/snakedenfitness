from django import forms
from django.contrib.auth.models import User
from .models import User, Profile, clientTrainer

# class RegistrationForm(UserCreationForm):
#     email = forms.EmailField(required=True)

#     class Meta:
#         model = Profile
#         fields = ['username', 'email', 'password1', 'password2', 'birth_date', 'bio', 'avatar']

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    # email = forms.CharField(widget=forms.EmailInput)
    # email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

class ProfileForm(forms.ModelForm):
    bio = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Profile
        fields = ('birth_date','bio', 'role', 'avatar')


    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        # self.fields['bio'].widget.attrs['style'] = 'width:400px; height:40px;'
        pass

    # def clean_client(self):
    #     if self.instance:
    #         return self.instance.client
    #     else:
    #         return self.fields['client']