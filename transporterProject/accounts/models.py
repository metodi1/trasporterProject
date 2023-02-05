from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.core import validators

from transporterProject.core.validators import validate_only_letters, MaxFileSizeInMBValidator


class TransportUser(AbstractUser):
    MAX_USER_NAME_LENGTH = 20
    MIN_USER_NAME_LENGTH = 2

    MAX_FIRST_NAME_LENGTH = 20
    MIN_FIRST_NAME_LENGTH = 2

    MAX_LAST_NAME_LENGTH = 20
    MIN_LAST_NAME_LENGTH = 2

    IMAGE_UPLOAD_TO_DIR = 'profiles/'

    first_name = models.CharField(max_length=MAX_FIRST_NAME_LENGTH,
                                  validators=(validators.MinLengthValidator(MIN_FIRST_NAME_LENGTH),
                                              validate_only_letters),
                                  null=True,
                                  blank=True,)
    last_name = models.CharField(max_length=MAX_LAST_NAME_LENGTH,
                                 validators=(validators.MinLengthValidator(MIN_LAST_NAME_LENGTH),
                                             validate_only_letters),
                                 null=True,
                                 blank=True,)

    profile_image = models.ImageField(
        upload_to='profiles/',
        null=True,
        blank=True,
        validators=(
            MaxFileSizeInMBValidator,
        )
    )

    user_name = models.CharField(max_length=MAX_USER_NAME_LENGTH,
                                 validators=[validators.MinLengthValidator(MIN_USER_NAME_LENGTH)],
                                             )

