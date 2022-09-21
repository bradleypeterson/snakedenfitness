from django.shortcuts import render


# Create your views here.
def community_home(request):
    return render(request, 'community/community_home.html', {})
