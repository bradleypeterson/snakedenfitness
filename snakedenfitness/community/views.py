from django.http import HttpResponse, FileResponse
from django.shortcuts import render, redirect
from .models import Room, Message, User, Invitation
from django.utils.text import slugify
from django.contrib import messages
from django.contrib.auth.decorators import permission_required, login_required
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .forms import Pic_Form
from .models import pic
from django.db import IntegrityError

@login_required
def room(request, slug):
    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room)[0:25]
    return render(request, 'community/room.html', {'room': room, 'messageList': messages})

@login_required
def rooms(request):
    rooms = Room.objects.filter(users__id=request.user.id)
    invites = Invitation.objects.filter(receiver=request.user.username)

    return render(request, 'community/rooms.html', {'rooms': rooms, 'invites': invites})

@login_required
def groupForm(request):
    if request.method == 'POST':
        try:
            group_name = request.POST.get('group_name')
            room_obj = Room.objects.create(name=group_name, slug=slugify(group_name))
            room_members = request.user.id
            room_obj.users.add(room_members)
        except IntegrityError:
            messages.add_message(request, messages.INFO, "Group name is taken")
            return render(request, 'community/groupForm.html', {})
        return redirect('rooms')
    return render(request, 'community/groupForm.html', {})

@login_required
def edit_group(request, name):
    room_obj = Room.objects.get(name=name)
    members = User.objects.all()
    if request.method == 'POST':
        member = request.POST.get('members', '')
        if User.objects.filter(username=member).exists():
            sender = request.user.username
            receiver = member
            group = name
            Invitation.objects.create(sender=sender, receiver=receiver, group=group)
        else:
            messages.add_message(request, messages.INFO, "User not found")

    return render(request, 'community/editGroup.html', {'room_obj': room_obj, 'members': members})


def accept_invite(request, group, id):
    room_obj = Room.objects.get(name=group)
    room_obj.users.add(request.user.id)
    invite = Invitation.objects.get(id=id)
    invite.delete()
    messages.add_message(request, messages.INFO, "Invite Accepted")
    return redirect('rooms')


def decline_invite(request, id):
    invite = Invitation.objects.get(id=id)
    invite.delete()
    messages.add_message(request, messages.INFO, "Invite Declined")
    return redirect('rooms')

def guides(request):
    form = Pic_Form()
    #path that it is showing /media/avatars/media/ERD_d9DHlWj.pdf

    if request.method == 'POST':
        form = Pic_Form(request.POST, request.FILES)
        if form.is_valid():
            user_pr_form = form.save(commit=False)
            user_pr_form.Upload = request.FILES['Upload']
            user_pr = str(user_pr_form.Upload)
            user_pr = user_pr.replace("avatars/", "")
            user_pr_form.save()
            return render(request, 'community/displayGuides.html', {'user_pr': user_pr})
    context = {"form": form}
    return render(request, 'community/guides.html', context)

@login_required
def displayGuides(request):
    return render(request, 'community/displayGuides.html', {})