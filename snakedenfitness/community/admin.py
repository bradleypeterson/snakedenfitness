from django.contrib import admin

from .models import Room, Message, Invitation

# Register your models here.
admin.site.register(Room)
admin.site.register(Message)
admin.site.register(Invitation)