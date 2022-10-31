from django import forms

class NewPostForm(forms.Form):
    postTitle = forms.CharField(max_length=100)
    content = forms.CharField(max_length=500)