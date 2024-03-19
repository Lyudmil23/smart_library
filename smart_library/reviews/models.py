from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator
from django.db import models

from smart_library.accounts.models import AppUser
from smart_library.books.models import Book


class Review(models.Model):
    DEFAULT_VALUE_REVIEW = 1.0
    MIN_VALUE_RATE = 1.0
    MAX_VALUE_RATE = 5.0
    MIN_LENGTH_COMMENT = 5

    user = models.ForeignKey(
        AppUser,
        on_delete=models.CASCADE,
    )

    book = models.ForeignKey(
        Book,
        related_name="reviews",
        on_delete=models.CASCADE,
    )

    rate = models.FloatField(
        default=DEFAULT_VALUE_REVIEW,
        validators=(
            MinValueValidator(MIN_VALUE_RATE),
            MaxValueValidator(MAX_VALUE_RATE),
        ),
    )

    comment = models.TextField(
        validators=(
            MinLengthValidator(MIN_LENGTH_COMMENT),
        ),
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return self.user.username
