import os

from django.db.models.signals import pre_delete
from django.dispatch import receiver

from smart_library.accounts.models import Profile


@receiver(pre_delete, sender=Profile)
def delete_profile_image(sender, instance, **kwargs):
    """
    A signal receiver which deletes the profile image when the profile is deleted.
    """
    if instance.profile_image:
        # Deleting the profile image from the media
        if os.path.isfile(instance.profile_image.path):
            os.remove(instance.profile_image.path)