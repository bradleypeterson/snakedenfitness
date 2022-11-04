from django import forms


class WorkoutForm(forms.Form):
    WORKOUT_TYPE = [
        ('Cardio', 'Cardio'),
        ('Strength', 'Strength'),
        ('Endurance', 'Endurance'),
    ]

    MUSCLE_GROUP = [
        ('Arms', 'Arms'),
        ('Shoulders', 'Shoulders'),
        ('Back', 'Back'),
        ('Core', 'Core'),
        ('Legs', 'Legs'),
    ]

    workout_type = forms.CharField(label='Select workout', widget=forms.Select(choices=WORKOUT_TYPE, attrs={'class': 'form-select huge'}))
    muscle_group = forms.CharField(label='Select muscle group', widget=forms.Select(choices=MUSCLE_GROUP, attrs={'class': 'form-select huge'}))
    exercise_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control huge', 'placeholder': 'Exercise Name'}))
    reps = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control huge', 'placeholder': 'Reps'}))
    sets = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control huge', 'placeholder': 'Sets'}))
    weight = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control huge', 'placeholder': 'Weight'}))
