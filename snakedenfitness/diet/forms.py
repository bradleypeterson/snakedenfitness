from django import forms


class MealForm(forms.Form):
    MEAL_TYPES = [
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
        ('snack', 'Snack'),
    ]

    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control huge', 'placeholder': 'Meal Name'}))
    meal_type = forms.CharField(label='Select meal type', widget=forms.Select(choices=MEAL_TYPES, attrs={'class': 'form-select huge'}))
    calories = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control huge', 'placeholder': 'Calories'}))
    carbs = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control huge', 'placeholder': 'Carbs'}))
    sugars = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control huge', 'placeholder': 'Sugars'}))
    protein = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control huge', 'placeholder': 'Protein'}))