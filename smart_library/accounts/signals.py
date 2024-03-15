import os

from django.db.models.signals import pre_delete, post_save
from django.dispatch import receiver

from smart_library.accounts.models import Profile, AppUser


@receiver(pre_delete, sender=Profile)
def delete_profile_image(sender, instance, **kwargs):
    """
    A signal receiver which deletes the profile image when the profile is deleted.
    """
    if instance.profile_image:
        # Deleting the profile image from the media
        if os.path.isfile(instance.profile_image.path):
            os.remove(instance.profile_image.path)


"""
When we are creating a new user from Django administration, automatically creation  of the corresponding profile.
"""
@receiver(post_save, sender=AppUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
