from django.shortcuts import render


# Create your views here.
def community_home(request):
    return render(request, 'community/community_home.html', {})

def new_post(request):
    return render(request, 'community/new_post.html', {})

def groups(request):
    return render(request, 'community/groups.html', {})

def edit_groups(request):
    return render(request, 'community/edit_groups.html', {})