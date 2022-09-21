from django.shortcuts import render


# Create your views here.
def fitness_home(request):
    return render(request, 'fitness/fitness_home.html', {})


def trainer_home(request):
    return render(request, 'fitness/trainer_home.html', {})
