# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import User, Group, AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
### Can set user permissions user.has_perm('app.add/change/delete/view')
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

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
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.Profile.save()


# can create user groups to manage permissions
# Dieticians, Trainers, and Clients. figure out family grouping laterrr
# user_group.permissions.set([permission_list])
# user_group.permissions.add(permission, permission, ...)
# user_group.permissions.remove(permission, permission, ...)
# user_group.permissions.clear()

client_group, created = Group.objects.get_or_create(name="Client")

diet_group, created = Group.objects.get_or_create(name="Dietician")

fit_group, created = Group.objects.get_or_create(name="Trainer")
