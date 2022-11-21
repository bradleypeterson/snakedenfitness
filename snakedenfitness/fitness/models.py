from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
# class TrainerProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     bio = models.TextField(max_length=500, blank=True)


class Workout(models.Model):
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

    workout_type = models.CharField(max_length=50, choices=WORKOUT_TYPE)
    muscle_group = models.CharField(max_length=50, choices=MUSCLE_GROUP)
    exercise_name = models.CharField(max_length=50)
    reps = models.IntegerField()
    sets = models.IntegerField()
    weight = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
