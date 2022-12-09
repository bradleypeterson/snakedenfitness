from django import forms
from .models import pic

class Pic_Form(forms.ModelForm):
    class Meta:
        model = pic
        fields = [
            'Upload',
        ]