# -*- coding: utf-8 -*-

from django import template
from django.db import models
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import User, Group, AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                primary_key=True)
    birth_date = models.DateField(blank=True, default='1960-01-01')
    bio = models.TextField(max_length=500, blank=True)
    avatar = models.ImageField(upload_to='avatars/',
                               null=True,
                               blank=True,
                               default='avatars/generic-avatar.png')

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

register = template.Library()

@register.filter(name="has_group")
def has_group(user, group_name):
    group =  Group.objects.get(name=group_name)
    return group in user.groups.all()

class clientDieter(models.Model):
    client = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        unique=True,
        related_name='D_assigned_client')

    dieter = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='D_assigned_dietician')

class clientTrainer(models.Model):
    client = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        unique=True,
        related_name='T_assigned_client')

    trainer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='T_assigned_trainer')
