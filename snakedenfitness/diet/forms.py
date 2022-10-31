from django import forms


class MealForm(forms.Form):
    MEAL_TYPES = [
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
        ('snack', 'Snack'),
    ]

    name = forms.CharField(max_length=100)
    meal_type = forms.CharField(label='Select meal type', widget=forms.Select(choices=MEAL_TYPES))
    calories = forms.IntegerField()
    carbs = forms.IntegerField()
    sugars = forms.IntegerField()
    protein = forms.IntegerField()

