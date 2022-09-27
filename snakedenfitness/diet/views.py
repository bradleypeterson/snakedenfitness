from django.shortcuts import render


# Create your views here.
def diet_home(request):
    return render(request, 'diet/diet_home.html', {})

# can restrict view here with permissions
# @permission_required('x.y') or PermissionRequiredMixin
def dietician_home(request):
    return render(request, 'diet/dietician_home.html', {})
