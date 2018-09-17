# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    lowercase_username = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.username