from django import forms
from .models import Meals

class MealForm2(forms.ModelForm):
    class Meta:
        model = Meals
        fields = ('meal_name', 'meal_type', 'calories', 'carbs', 'sugars', 'protein')