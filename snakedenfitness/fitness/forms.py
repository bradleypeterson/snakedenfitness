from django import forms

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
    
    workout_type = forms.CharField(label='Select workout', widget=forms.Select(choices=WORKOUT_TYPE))
    muscle_group = forms.CharField(label='Select muscle group', widget=forms.Select(choices=MUSCLE_GROUP))
    exercise_name = forms.CharField()
    reps = forms.IntegerField()
    sets = forms.IntegerField()
    weight = forms.IntegerField()