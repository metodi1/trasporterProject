from django.core import exceptions
from django.core.exceptions import ValidationError


def validate_only_letters(value):
    for ch in value:
        if not ch.isalpha():
            raise exceptions.ValidationError('Only letters are allowed')


LIMIT_SIZE_IN_MB = 5


def MaxFileSizeInMBValidator(value):
    limit = LIMIT_SIZE_IN_MB * 1024 * 1024
    if value.file.size > limit:
        raise ValidationError(f'Max file size is {LIMIT_SIZE_IN_MB:.2f} MB')
