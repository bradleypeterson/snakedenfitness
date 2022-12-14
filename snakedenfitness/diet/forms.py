from django import forms
from django.forms import ModelForm
from .models import Meal
from users.models import clientDieter, Profile, User

class MealForm(ModelForm):
    class Meta:
        model = Meal
        fields = ('meal_name', 'meal_type', 'calories', 'carbs', 'sugars', 'protein')

        MEAL_TYPES = [
            ('Breakfast', 'Breakfast'),
            ('Lunch', 'Lunch'),
            ('Dinner', 'Dinner'),
            ('Snack', 'Snack'),
        ]
        labels = {
            'meal_name': 'Meal Name',
            'meal_type': 'Meal Type',
            'calories': 'Calories',
            'carbs': 'Carbs',
            'sugars': 'Sugars',
            'protein': 'Protein',
        }
        widgets = {
            'meal_name': forms.TextInput({'class': 'form-control', 'placeholder': 'Meal Name'}),
            'meal_type': forms.Select(choices=MEAL_TYPES, attrs={'class': 'form-select huge'}),
            'calories': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Calories'}),
            'carbs': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Carbs'}),
            'sugars': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sugars'}),
            'protein': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Protein'}),
        }


class clientDieterForm(forms.ModelForm):
    class Meta:
        model = clientDieter
        fields = ('client', 'dieter')

    def __init__(self, *args, **kwargs):
        super(clientDieterForm, self).__init__(*args, **kwargs)
        self.fields['client'].widget.attrs['readonly'] = True
        pass
