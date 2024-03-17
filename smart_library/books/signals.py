import os

from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

from smart_library.books.models import Book


@receiver(models.signals.post_delete, sender=Book)
def delete_book_image(sender, instance, **kwargs):
    """
    Deletes book image from media when corresponding Book object is deleted.
    """
    if instance.book_image:
        if os.path.isfile(instance.book_image.path):
            os.remove(instance.book_image.path)


@receiver(pre_save, sender=Book)
def update_book_image(sender, instance, **kwargs):
    """
    Deletes old book_image from media
    when corresponding `Book` object is updated with a new image.
    """
    if instance.pk:  # if the book exists
        old_image = Book.objects.get(pk=instance.pk).book_image
        # if a new image file has been uploaded and it's different from the old one
        if instance.book_image and old_image != instance.book_image:
            if os.path.isfile(old_image.path):
                os.remove(old_image.path)