from django.db import models
from django.conf import settings

# Create your models here.
from django.contrib.auth.models import User

class Room(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    users = models.ManyToManyField(User)

class Message(models.Model):
    room = models.ForeignKey(Room, related_name='messages', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date_added',)

class Invitation(models.Model):
    sender = models.CharField(max_length=255)
    receiver = models.CharField(max_length=255)
    group = models.CharField(max_length=255)

class pic(models.Model):
    Upload = models.FileField(upload_to="avatars/")