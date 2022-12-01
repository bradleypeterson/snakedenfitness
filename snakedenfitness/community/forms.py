from django import forms
from .models import pic

class Profile_Form(forms.ModelForm):
    class Meta:
        model = pic
        fields = [
            'display_picture'
        ]