from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib import messages

#from .forms import NameForm
from .forms import MealForm, clientDieterForm
from .models import Meal
from users.models import Profile as UProfile, User as UUser, clientDieter as ClientDiet

@login_required
def diet_home(request):
    meal = Meal.objects.all()
    return render(request, 'diet/diet_home.html', {'meal': meal})

@login_required
def dietitian_home(request):
    CTtable = ClientDiet.objects.filter(dieter = request.user)
    return render(request, 'diet/dietitian_home.html', {'CTtable' : CTtable})

@login_required
def meal_form(request):
    # This needs to be fixed. Was crashing Meal Form
    #total = MealForm.calories
    total = 0

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
            return HttpResponseRedirect('/diet/')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = MealForm()

    context = {
        'form': form,
        'total': total,
    }

    return render(request, 'diet/meal_form.html', context)

@login_required
def update_profile(request, user_id):
    user = User.objects.get(pk=user_id)
    user.profile.bio = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit...'
    user.save()

@login_required
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
    CDTable = ClientDiet.objects.filter(dieter = request.user)
    return render(request, 'diet/pro_meal_log.html', {'meals': meals, 'CDTable': CDTable})

######## Client-Professional Relationship
@login_required
def request_dietician(request):
    listAllUsers = UUser.objects.all()
    listCliDies = ClientDiet.objects.all()
    listAllDieticians = UProfile.objects.filter(role=1)

    if request.method == 'POST':
        CDForm = clientDieterForm(request.POST, initial={'client' : request.user})
        CDForm.fields['client'].disabled = True
        CDForm.fields['dieter'].queryset = User.objects.filter(profile__in=listAllDieticians)

        if CDForm.is_valid():
                CDForm.save()
                messages.success(request, (' Dietitian added '))
                return redirect('/diet/')
        else:
            messages.error(request, ('Error adding dietician'))

    else:
        CDForm = clientDieterForm(initial={'client' : request.user})
        CDForm.fields['client'].disabled = True
        CDForm.fields['dieter'].queryset = User.objects.filter(profile__in=listAllDieticians)


    return render(request, 'diet/add_diet_form.html', {
        'form': CDForm,
        'listAllUsers' : listAllUsers,
        'listCliDies' : listCliDies,
        'listAllDieticians' : listAllDieticians
        })


@login_required
def update_dietician(request):
    return render(request, 'diet/request_dietician.html', {})

@login_required
def delete_dietician(request, client_id):
    cliDie = ClientDiet.objects.get(id=client_id)
    listCliDies = ClientDiet.objects.get(dieter=request.user, client=cliDie.client)

    if request.method == 'POST':
        CTForm = clientDieterForm(request.POST, instance=listCliDies)
        CTForm.fields['client'].disabled = True
        CTForm.fields['dieter'].disabled = True


        if CTForm.is_valid():
            cliDie.delete()
            messages.success(request, ('Clients updated'))
            return redirect('/diet/')
        else:
            messages.error(request, ('Error'))

    else:
       CTForm = clientDieterForm(instance=listCliDies)
       CTForm.fields['client'].disabled = True
       CTForm.fields['dieter'].disabled = True

    return render(request, 'diet/delete_diet_form.html', {
        'form': CTForm,
        'listCliDies' : listCliDies,
        })
