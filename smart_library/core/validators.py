from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator


def validate_only_letters(value):
    if not value.isalpha():
        raise ValidationError('The name should contain only letters!')


validate_book_name = RegexValidator(r'^[a-zA-Z\s]*$', 'The name should contain only letters!')