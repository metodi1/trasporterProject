from django.core import validators
from django.db import models

# Create your models here.
from django.db import models
from django.contrib import auth

from transporterProject.accounts.models import TransportUser


class TransportersLikes(models.Model):
    class Meta:
        ordering = ['transporter']

    transporter = models.CharField(max_length=30)
    liker_today = models.CharField(max_length=30)
    date_of_like = models.DateField(auto_now_add=True)
