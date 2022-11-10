from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import permission_required, login_required
from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import WorkoutForm, clientTrainerForm
from .models import Workout


from users.models import Profile as UProfile, User as UUser, clientTrainer as CT


# Create your views here.

# can restrict view here with permissions
# @permission_required('x.y') or PermissionRequiredMixin

@login_required
def fitness_home(request):
    CTtable = CT.objects.filter(client = request.user)

    return render(request, 'fitness/fitness_home.html', {'CTtable' : CTtable})

@login_required
def trainer_home(request):
    CTtable = CT.objects.filter(trainer = request.user)
    return render(request, 'fitness/trainer_home.html', {'CTtable' : CTtable})

@login_required
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
            obj.user = User(request.user.id)
            obj.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/fitness/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = WorkoutForm()

    return render(request, 'fitness/workout_form.html', {'form': form})


@login_required
def update_profile(request, user_id):
    user = User.objects.get(pk=user_id)
    user.profile.bio = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit...'
    user.save()


@login_required
def user_workout_data(request):
    workouts = Workout.objects.filter(user=request.user)
    return render(request, 'fitness/workout_log.html', {'workouts': workouts})

@login_required
def trainer_workout_data(request):
    workouts = Workout.objects.all()
    CTtable = CT.objects.filter(trainer = request.user)

    return render(request, 'fitness/pro_workout_log.html', {'workouts': workouts, 'CTtable': CTtable})



@login_required
def add_client(request):
    trainerU = UUser.objects.all()
    tc = CT.objects.all()
    Xtrain = UProfile.objects.filter(role=2)

    return render(request, 'fitness/add_client.html', {
        'trainerU': trainerU,
        'client': tc,
        'Xtrain': Xtrain
        })


@login_required
def clientTrainer_form(request):
    listUsers = UUser.objects.all()
    listTrainersClients = CT.objects.all()
    listTrainers = UProfile.objects.filter(role=2)

    if request.method == 'POST':
        CTForm = clientTrainerForm(request.POST, initial={'client': request.user})
        CTForm.fields['client'].disabled = True

        if CTForm.is_valid():
            CTForm.save()
            messages.success(request, (' Trainer added'))
            return redirect('/fitness/')
        else:
            messages.error(request, ('Error'))

    else:
       CTForm = clientTrainerForm(initial={'client': request.user})
       CTForm.fields['client'].disabled = True

    return render(request, 'fitness/add_client_form.html', {
        'form': CTForm,
        'listUsers' : listUsers,
        'listTrainersClients' : listTrainersClients,
        'listTrainers' : listTrainers
        })

@login_required
def clientTrainer_update(request):

    if request.user.profile.role == 2:
        listTrainersClients = CT.objects.get(trainer=request.user)
    else:
        listTrainersClients = CT.objects.get(client=request.user)

    listTrainers = UProfile.objects.filter(role=2)

    if request.method == 'POST':
        CTForm = clientTrainerForm(request.POST, instance=listTrainersClients)
        CTForm.fields['client'].disabled = True

        if CTForm.is_valid():
            CTForm.save()
            messages.success(request, ('Trainer updated'))
            return redirect('/fitness/')
        else:
            messages.error(request, ('Error'))

    else:
       CTForm = clientTrainerForm(instance=listTrainersClients)
       CTForm.fields['client'].disabled = True

    return render(request, 'fitness/update_client_form.html', {
        'form': CTForm,
        'listTrainersClients' : listTrainersClients,
        'listTrainers' : listTrainers
        })


@login_required
def clientTrainer_delete(request, client_id):

    cliTrain = CT.objects.get(id=client_id)


    listTrainersClients = CT.objects.get(trainer=request.user, client=cliTrain.client)


    if request.method == 'POST':
        CTForm = clientTrainerForm(request.POST, instance=listTrainersClients)
        CTForm.fields['client'].disabled = True
        CTForm.fields['trainer'].disabled = True


        if CTForm.is_valid():
            cliTrain.delete()
            messages.success(request, ('Clients updated'))
            return redirect('/fitness/')
        else:
            messages.error(request, ('Error'))

    else:
       CTForm = clientTrainerForm(instance=listTrainersClients)
       CTForm.fields['client'].disabled = True
       CTForm.fields['trainer'].disabled = True

    return render(request, 'fitness/delete_client_form.html', {
        'form': CTForm,
        'listTrainersClients' : listTrainersClients,
        })