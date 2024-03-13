from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from smart_library.accounts.managers import AppUserManager


class AppUser(AbstractBaseUser, PermissionsMixin):
    MAX_LENGTH_USERNAME = 30

    username = models.CharField(
        max_length=MAX_LENGTH_USERNAME,
        unique=True,
    )

    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    is_active = models.BooleanField(
        default=True,
    )

    is_staff = models.BooleanField(
        default=False,
        null=False,
        blank=False,
    )

    is_superuser = models.BooleanField(
        default=False,
        null=False,
        blank=False,
    )

    USERNAME_FIELD = 'username'

    objects = AppUserManager()
