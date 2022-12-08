from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from datetime import datetime, timedelta, time

from .forms import MealForm
from .models import Meal


@login_required
def diet_home(request):
    today = datetime.today()

    year = today.year
    month = today.month
    day = today.day

    filter = Meal.objects.filter(created_at__year=year,
                               created_at__month=month, created_at__day=day)

    meal = Meal.objects.all()

    total_sum = 0

    for item in filter:
        total_sum += item.calories

    return render(request, 'diet/diet_home.html', {'meal': meal, 'total_sum': total_sum, 'filter': filter})


@login_required
def dietitian_home(request):
    return render(request, 'diet/dietitian_home.html', {})


@login_required
def meal_form(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = MealForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            obj = Meal()
            obj.meal_name = form.cleaned_data['meal_name']
            obj.meal_type = form.cleaned_data['meal_type']
            obj.calories = form.cleaned_data['calories']
            obj.carbs = form.cleaned_data['carbs']
            obj.sugars = form.cleaned_data['sugars']
            obj.protein = form.cleaned_data['protein']
            obj.user = User(request.user.id)
            obj.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/diet/meal_log/')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = MealForm()

    return render(request, 'diet/meal_form.html', {'form': form})


@login_required
def update_profile(request, user_id):
    user = User.objects.get(pk=user_id)
    user.profile.bio = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit...'
    user.save()


def request_dietician(request):
    return render(request, 'diet/request_dietician.html', {})


def delete_meal(request, id):
        meal = Meal.objects.get(pk=id)
        meal.delete()
        return redirect('diet_home')


@login_required
def edit_meal(request, id):
    meal = Meal.objects.get(pk=id)
    form = MealForm(request.POST or None, instance=meal)

    if form.is_valid():
        form.save()
        return redirect('diet_home')

    return render(request, 'diet/edit_meal.html', {'meal': meal, 'form': form})


@login_required
def user_meal_data(request):
    meals = Meal.objects.filter(user=request.user)
    return render(request, 'diet/meal_log.html', {'meals': meals})


@login_required
def trainer_meal_data(request):
    meals = Meal.objects.all()
    return render(request, 'diet/pro_meal_log.html', {'meals': meals})
