from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def diet_home(request):
    return render(request, 'diet/diet_home.html', {})

# can restrict view here with permissions
# @permission_required('x.y') or PermissionRequiredMixin
def dietitian_home(request):
    return render(request, 'diet/dietitian_home.html', {})


def update_profile(request, user_id):
    user = User.objects.get(pk=user_id)
    user.profile.bio = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit...'
    user.save()
