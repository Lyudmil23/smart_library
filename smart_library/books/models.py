import datetime
import uuid

from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from smart_library.accounts.models import AppUser
from smart_library.authors.models import Author
from smart_library.categories.models import Category
from smart_library.core.validators import validate_book_name


class Book(models.Model):
    MIN_LENGTH_BOOK_TITLE = 2
    MIN_VALUE_BOOK_PRICE = 1

    IMAGE_UPLOAD_TO_DIR = 'books/'

    book_title = models.CharField(
        max_length=50,
        unique=True,
        validators=(
            MinLengthValidator(MIN_LENGTH_BOOK_TITLE),
            validate_book_name,
        ),
    )

    book_image = models.ImageField(
        upload_to=IMAGE_UPLOAD_TO_DIR,
        null=False,
        blank=False,
    )

    description = models.TextField(
        null=False,
        blank=False,
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
    )

    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='books',
    )

    serial = models.CharField(
        max_length=30,
        unique=True,
        editable=False,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    price = models.FloatField(
        validators=(
            MinValueValidator(MIN_VALUE_BOOK_PRICE),
        ),
    )

    def __str__(self):
        return self.book_title

    def save(self, *args, **kwargs):
        if not self.serial:
            while True:
                serial = uuid.uuid4().hex[:12].upper()
                if not Book.objects.filter(serial=serial).exists():
                    break
            self.serial = serial

        super().save(*args, **kwargs)

    # class Meta:
    #     ordering = ('id', )


class RentBook(models.Model):
    user = models.ForeignKey(
        AppUser,
        on_delete=models.CASCADE,
    )
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    period_start = models.DateField()
    period_end = models.DateField()

    def clean(self):
        current_date = datetime.date.today()
        if self.period_start < current_date:
            raise ValidationError("Period start cannot be a date earlier than today.")
        if self.period_start > self.period_end:
            raise ValidationError("Period start cannot be later than Period end.")
        super().clean()

    def __str__(self):
        return self.user.username