from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import permission_required


from .forms import WorkoutForm
from .models import Workout


# Create your views here.
def fitness_home(request):
    return render(request, 'fitness/fitness_home.html', {})


# can restrict view here with permissions
# @permission_required('x.y') or PermissionRequiredMixin
def trainer_home(request):
    return render(request, 'fitness/trainer_home.html', {})


def workout_form(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = WorkoutForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            obj = Workout()
            obj.workout_type = form.cleaned_data['workout_type']
            obj.muscle_group = form.cleaned_data['muscle_group']
            obj.exercise_name = form.cleaned_data['exercise_name']
            obj.reps = form.cleaned_data['reps']
            obj.sets = form.cleaned_data['sets']
            obj.weight = form.cleaned_data['weight']
            obj.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/fitness/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = WorkoutForm()

    return render(request, 'fitness/workout_form.html', {'form': form})


def update_profile(request, user_id):
    user = User.objects.get(pk=user_id)
    user.profile.bio = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit...'
    user.save()