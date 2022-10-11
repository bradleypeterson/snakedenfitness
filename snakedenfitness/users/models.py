# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from unicodedata import name
from venv import create

from django.db import models

from django.contrib.auth.models import User, Group

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nameFirst = models.CharField(max_length=50)
    nameLast = models.CharField(max_length=50)

    # Can set user permissions user.has_perm('app.add/change/delete/view')

# can create user groups to manage permissions
# Dieticians, Trainers, and Clients. figure out family grouping laterrr
client_group, created = Group.objects.get_or_create(name="client")
    # user_group.permissions.set([permission_list])
    # user_group.permissions.add(permission, permission, ...)
    # user_group.permissions.remove(permission, permission, ...)
    # user_group.permissions.clear()

diet_group, created = Group.objects.get_or_create(name="dietician")


fit_group, created = Group.objects.get_or_create(name="trainer")
