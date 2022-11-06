from django.shortcuts import render, redirect
from .models import Room, Message, User
from django.utils.text import slugify


# Create your views here.
def community_home(request):
    return render(request, 'community/community_home.html', {})


def room(request, slug):
    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room)[0:25]
    return render(request, 'community/room.html', {
        'room': room,
        'messageList': messages
    })


def rooms(request):
    rooms = Room.objects.filter(users__id=request.user.id)

    return render(request, 'community/rooms.html', {'rooms': rooms})


def groupForm(request):
    if request.method == 'POST':
        group_name = request.POST.get('group_name')
        room_obj = Room.objects.create(name=group_name, slug=slugify(group_name))
        room_members = request.user.id
        room_obj.users.add(room_members)
        return redirect('rooms')
    return render(request, 'community/groupForm.html', {})
