from django.core.validators import MinLengthValidator
from django.db import models

from smart_library.core.validators import validate_only_letters


class Category(models.Model):
    MIN_LENGTH_CATEGORY = 3
    MAX_LENGTH_CATEGORY = 30

    name = models.CharField(
        max_length=MAX_LENGTH_CATEGORY,
        unique=True,
        validators=(
            MinLengthValidator(MIN_LENGTH_CATEGORY),
            validate_only_letters,
        ),
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

