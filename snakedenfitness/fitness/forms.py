from django import forms
from .models import Workout
from django.forms import ModelForm


class WorkoutForm(ModelForm):
    class Meta:
        model = Workout
        fields = ('workout_type', 'muscle_group', 'exercise_name', 'reps', 'sets', 'weight')
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
    labels = {
        'workout_type': 'Workout Type',
        'muscle_group': 'Muscle Group',
        'exercise_name': '',
        'reps': 'Reps',
        'sets': 'Sets',
        'weight': 'Weight',
    }
    widgets = {
        'workout_type': forms.Select(choices=WORKOUT_TYPE, attrs={'class': 'form-select'}),
        'muscle_group':forms.Select(choices=MUSCLE_GROUP, attrs={'class': 'form-select'}),
        'exercise_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Exercise Name'}),
        'reps': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Reps'}),
        'sets': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sets'}),
        'weight': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Weight'}),
    }