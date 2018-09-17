# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):

    def __str__(self):
        return self.username
