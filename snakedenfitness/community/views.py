from django.shortcuts import render


# Create your views here.
def community_home(request):
    return render(request, 'community/community_home.html', {})


def room(request, room_name):
    return render(request, 'community/room.html', {
        'room_name': room_name
    })
