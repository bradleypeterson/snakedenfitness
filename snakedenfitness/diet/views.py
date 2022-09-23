from django.shortcuts import render


# Create your views here.
def diet_home(request):
    return render(request, 'diet/diet_home.html', {})


def dietician_home(request):
    return render(request, 'diet/dietician_home.html', {})
