# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    # add additional fields in here

    def __str__(self):
        return self.username