from django import forms
from users.models import clientTrainer

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



class clientTrainerForm(forms.ModelForm):
    # client = forms.ChoiceField(widget=forms.ChoiceField)
    class Meta:
        model = clientTrainer
        fields = ('client', 'trainer')

    def __init__(self, *args, **kwargs):
        super(clientTrainerForm, self).__init__(*args, **kwargs)
        self.fields['client'].widget.attrs['readonly'] = True
        pass
