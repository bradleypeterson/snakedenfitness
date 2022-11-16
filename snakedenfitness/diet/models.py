from django.db import models
from django import template
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import date, datetime
from django.core.exceptions import ValidationError


# Verify Age Requirement in registration form
# https://www.geeksforgeeks.org/python-program-to-calculate-age-in-year/
def validate_dob(dob):
    # Today's Date
    today = date.today()

    # Age = Today's year minus birth year - (The greater month / day tuple)
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

    # Throw validation error if age is < 12
    if age < 12:
        raise ValidationError("Must be at least 12 years old to register")
    return dob


class DietitianProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(default="John", max_length=100)
    last_name = models.CharField(default="Doe", max_length=100)
    dob = models.DateField(
        verbose_name="birthdate", max_length=8, validators=[validate_dob]
    )
    email = models.EmailField(max_length=200, null=True)
    bio = models.TextField(max_length=500, blank=True)
    # image = models.ImageField(default="/defaults/profile.png", upload_to="profiles")
    # client = models.ManyToManyField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


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

    created_at = models.DateTimeField()


register = template.Library()

@register.simple_tag
def meals_by_user():
    pass
