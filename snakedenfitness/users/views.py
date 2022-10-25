# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import transaction
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from .models import Profile
from .forms import UserForm, ProfileForm
from django.contrib import messages
from django.contrib.auth.hashers import make_password

from diet.models import Meal
from fitness.models import Workout


# Create your views here.
def register(request):
    # if request.method == 'POST':
    #     form = RegistrationForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         username = form.cleaned_data.get('username')
    #         messages.success(request, f'User {username} successfully created')
    #         return redirect('login')

    # else:
    #     form = RegistrationForm()

    # return render(request, 'users/register.html', {'form':form})
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            passw = user_form.save(commit = False)
            passw.set_password(user_form.cleaned_data['password'])

            user = user_form.save()

            profile = profile_form.save(commit = False)
            profile.user = user
            img = request.FILES['avatar']
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

    return render(request, 'users/profile.html', {})


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
    return render(request, 'users/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
