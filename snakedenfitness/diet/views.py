from django.shortcuts import render
from django.contrib.auth.models import User


def diet_home(request):
    return render(request, 'diet/diet_home.html', {})


def dietitian_home(request):
    return render(request, 'diet/dietitian_home.html', {})


def update_profile(request, user_id):
    user = User.objects.get(pk=user_id)
    user.profile.bio = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit...'
    user.save()