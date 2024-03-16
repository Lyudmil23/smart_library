import datetime

from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models

from smart_library.core.validators import validate_only_letters


class Author(models.Model):
    MIN_LENGTH_AUTHOR_NAME = 2
    MAX_LENGTH_AUTHOR_NAME = 30

    first_name = models.CharField(
        max_length=MAX_LENGTH_AUTHOR_NAME,
        validators=(
            MinLengthValidator(MIN_LENGTH_AUTHOR_NAME),
            validate_only_letters,
        ),
        null=False,
        blank=False,
    )

    last_name = models.CharField(
        max_length=MAX_LENGTH_AUTHOR_NAME,
        validators=(
            MinLengthValidator(MIN_LENGTH_AUTHOR_NAME),
            validate_only_letters,
        ),
        null=False,
        blank=False,
    )

    date_of_birth = models.DateField()

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def clean(self):
        current_date = datetime.date.today()
        if self.date_of_birth > current_date:
            raise ValidationError("Birthday cannot be in the future.")
        super().clean()

    class Meta:
        unique_together = ('first_name', 'last_name', )

