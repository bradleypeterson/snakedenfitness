from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def fitness_home(request):
    return render(request, 'fitness/fitness_home.html', {})


def trainer_home(request):
    return render(request, 'fitness/trainer_home.html', {})


def update_profile(request, user_id):
    user = User.objects.get(pk=user_id)
    user.profile.bio = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit...'
    user.save()