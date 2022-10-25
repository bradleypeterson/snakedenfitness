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


class WorkoutForm(forms.Form):
    WORKOUT_TYPE = [
        ('cardio', 'Cardio'),
        ('strength', 'Strength'),
        ('endurance', 'Endurance'),
    ]

    MUSCLE_GROUP = [
        ('arms', 'Arms'),
        ('shoulders', 'Shoulders'),
        ('back', 'Back'),
        ('core', 'Core'),
        ('legs', 'Legs'),
    ]

    workout_type = forms.CharField(label="Select workout type", widget=forms.Select(choices=WORKOUT_TYPE))
    muscle_group = forms.CharField(label="Select muscle group", widget=forms.Select(choices=MUSCLE_GROUP))
    exercise_name = forms.CharField(max_length=50)
    reps = forms.IntegerField()
    sets = forms.IntegerField()
    weight = forms.IntegerField()
