import os

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import MinLengthValidator
from django.db import models

from smart_library.accounts.managers import AppUserManager
from smart_library.core.validators import validate_only_letters


class AppUser(AbstractBaseUser, PermissionsMixin):
    MAX_LENGTH_USERNAME = 30
    MIN_LENGTH_USERNAME = 3

    username = models.CharField(
        max_length=MAX_LENGTH_USERNAME,
        validators=(
            MinLengthValidator(MIN_LENGTH_USERNAME),
        ),
        unique=True,
        null=False,
        blank=False,
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


class Profile(models.Model):
    CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Do not show', 'Do not show'),
    )

    MIN_LENGTH_FIRST_NAME = 2
    MAX_LENGTH_FIRST_NAME = 30

    MIN_LENGTH_LAST_NAME = 2
    MAX_LENGTH_LAST_NAME = 30

    MAX_LENGTH_GENDER = 15

    IMAGE_UPLOAD_TO_DIR = 'profiles/'

    first_name = models.CharField(
        max_length=MAX_LENGTH_FIRST_NAME,
        validators=(
            MinLengthValidator(MIN_LENGTH_FIRST_NAME),
            validate_only_letters,
        ),
        null=False,
        blank=False,
    )

    last_name = models.CharField(
        max_length=MAX_LENGTH_LAST_NAME,
        validators=(
            MinLengthValidator(MIN_LENGTH_LAST_NAME),
            validate_only_letters,
        ),
        null=False,
        blank=False,
    )

    gender = models.CharField(
        max_length=MAX_LENGTH_GENDER,
        choices=CHOICES,
        null=True,
        blank=True,
    )

    profile_image = models.ImageField(
        upload_to=IMAGE_UPLOAD_TO_DIR,
        null=True,
        blank=True,
    )

    user = models.OneToOneField(
        AppUser,
        primary_key=True,
        on_delete=models.CASCADE,
    )

    def save(self, *args, **kwargs):
        try:
            existing_profile = Profile.objects.get(pk=self.pk)
            if existing_profile.profile_image != self.profile_image:
                # If profile exists and profile image is updated, we are deleting the old image
                if existing_profile.profile_image:
                    os.remove(existing_profile.profile_image.path)
        except Profile.DoesNotExist:
            pass

        super().save(*args, **kwargs)