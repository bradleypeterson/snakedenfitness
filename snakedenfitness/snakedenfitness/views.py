from django.shortcuts import render
from fitness.models import Workout
from diet.models import Meal
from community.models import Room
from datetime import datetime, timedelta
import pytz


# Create your views here.
def index(request):
    today = datetime.today()
    year = today.year
    month = today.month
    day = today.day
    one_week_ago = datetime.today() - timedelta(days=7)
    cardio, strength, endurance, total_calories, breakfast_cal, lunch_cal, dinner_cal, snack_cal = 0, 0, 0, 0, 0, 0, 0, 0
    workouts = Workout.objects.filter(created_at__gte=one_week_ago, user=request.user)
    daily_meals = Meal.objects.filter(created_at__year=year, created_at__month=month, created_at__day=day)
    rooms = Room.objects.filter(users__id=request.user.id)

    for workout in workouts:
        print("workout type", workout.workout_type)
        if workout.workout_type == 'Cardio':
            cardio += workout.sets*workout.reps
        elif workout.workout_type == 'Strength':
            strength += workout.sets*workout.reps
        elif workout.workout_type == 'Endurance':
            endurance += workout.sets*workout.reps

    for item in daily_meals:
        total_calories += item.calories
        if item.meal_type == 'Breakfast':
            breakfast_cal += item.calories
        elif item.meal_type == 'Lunch':
            lunch_cal += item.calories
        elif item.meal_type == 'Dinner':
            dinner_cal += item.calories
        elif item.meal_type == 'Snack':
            snack_cal += item.calories

    return render(request, 'index.html', {
        'cardio': cardio,
        'strength': strength,
        'endurance': endurance,
        'total_calories': total_calories,
        'breakfast_cal': breakfast_cal,
        'lunch_cal': lunch_cal,
        'dinner_cal': dinner_cal,
        'snack_cal': snack_cal,
        'rooms': rooms
    })
