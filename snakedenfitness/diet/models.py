from django.db import models
from django import template
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import date, datetime
from django.core.exceptions import ValidationError


# # Verify Age Requirement in registration form
# # https://www.geeksforgeeks.org/python-program-to-calculate-age-in-year/
def validate_dob(dob):
    # Today's Date
    today = date.today()

    # Age = Today's year minus birth year - (The greater month / day tuple)
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

    # Throw validation error if age is < 12
    if age < 12:
        raise ValidationError("Must be at least 12 years old to register")
    return dob

class clientDieter(models.Model):
    client = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        unique=True,
        related_name='assigned_diet_client')

    dieter = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='assigned_dietician')

class Meal(models.Model):
    MEAL_TYPES = [
        ('Breakfast', 'Breakfast'),
        ('Lunch', 'Lunch'),
        ('Dinner', 'Dinner'),
        ('Snack', 'Snack'),
    ]

    meal_name = models.CharField(max_length=100)
    meal_type = models.CharField(max_length=50, choices=MEAL_TYPES)
    calories = models.IntegerField()
    carbs = models.IntegerField()
    sugars = models.IntegerField()
    protein = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default='2006-10-25 14:30:59')


register = template.Library()


@register.simple_tag
def meals_by_user():
    pass