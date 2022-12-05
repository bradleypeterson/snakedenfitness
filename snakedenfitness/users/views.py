# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import transaction
from django.db.models import Max
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from .models import Profile
from .forms import UserForm, ProfileForm
from django.contrib import messages
from django.contrib.auth.hashers import make_password

from diet.models import Meal
from fitness.models import Workout
from users.models import Profile, User, clientTrainer


# Create your views here.
def register(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            passw = user_form.save(commit=False)
            passw.set_password(user_form.cleaned_data['password'])

            user = user_form.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            img = request.FILES.get('avatar', 'generic-avatar.png')
            profile.avatar = img

            profile.save()

            username = user_form.cleaned_data.get('username')

            messages.success(request, f'User {username} successfully created')
            return redirect('login')
        else:
            messages.error(request, ('Error on submit'))

    else:
        user_form = UserForm()
        profile_form = ProfileForm()

    return render(request, 'users/register.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


@login_required
def profile(request):
    #print(f"REQUEST: {request.user.profile.avatar}")
    avatar_loc = request.user.profile.avatar.url
    split_avatar = avatar_loc.replace("avatars/", "")
    profile_avatar = split_avatar.replace("/media/", "")
    #print(f"PROFILE AVATAR: {profile_avatar}")
    CTtable = clientTrainer.objects.filter(client=request.user)
    if request.user.profile.role == 2:
        CTtable = clientTrainer.objects.filter(trainer=request.user)
    return render(request, 'users/profile.html', {'CTtable': CTtable, 'profile_avatar': profile_avatar})


@login_required
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES,  instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, (' profile  updated'))
            return redirect('login')
        else:
            messages.error(request, ('Error'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'users/update_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


@login_required
def user_meal_data(request):
    meals = Meal.objects.filter(user=request.user)
    return render(request, 'users/meal_log.html', {'meals': meals})


@login_required
def user_workout_data(request):
    workouts = Workout.objects.filter(user=request.user)

    prs = []
    muscle_group = ['arms', 'back', 'shoulders', 'core', 'legs']
    for muscle in muscle_group:
        workout1 = Workout.objects.filter(user=request.user, muscle_group=muscle)
        pr1 = workout1.order_by('-weight').first()
        if pr1 is not None:
            prs.append(pr1.weight)

    return render(request, 'users/workout_log.html', {'workouts': workouts, 'prs': prs})


