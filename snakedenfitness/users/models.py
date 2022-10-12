# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import User, Group, AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
### Can set user permissions user.has_perm('app.add/change/delete/view')

# class User(AbstractUser):
#     pass

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    birth_date = models.DateField(blank=True, default='1960-01-01')
    bio = models.TextField(max_length=500, blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True, default='avatars/generic-avatar.png')

    CLIENT = 0
    DIETICIAN = 1
    TRAINER = 2

    ROLE_CHOICES = (
        (CLIENT, 'Client'),
        (DIETICIAN, 'Dietician'),
        (TRAINER, 'Trainer'),
    )

    role = models.SmallIntegerField(choices=ROLE_CHOICES, blank=True, null=False, default = 0)

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
# post_save.connect(create_user_profile, sender=User)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()


# need to create CUSTOM PERMISSIONS

# can create user groups to manage permissions
# Dieticians, Trainers, and Clients. figure out family grouping laterrr
# user_group.permissions.set([permission_list])
# user_group.permissions.add(permission, permission, ...)
# user_group.permissions.remove(permission, permission, ...)
# user_group.permissions.clear()

# client_group, created = Group.objects.get_or_create(name="Client")

# diet_group, created = Group.objects.get_or_create(name="Dietician")

# fit_group, created = Group.objects.get_or_create(name="Trainer")
