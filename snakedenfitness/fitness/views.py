from django.shortcuts import render
from django.contrib.auth.decorators import permission_required

# Create your views here.
def fitness_home(request):
    return render(request, 'fitness/fitness_home.html', {})

# can restrict view here with permissions
# @permission_required('x.y') or PermissionRequiredMixin
def trainer_home(request):
    return render(request, 'fitness/trainer_home.html', {})
