from django.core import validators
from django.db import models

# Create your models here.
from django.db import models
from django.contrib import auth

from transporterProject.accounts.models import TransportUser

# Create your models here.
MIN_LINE_NAME_LENGTH = 2


class Production_line(models.Model):
    line_name = models.CharField(max_length=10, unique=True,
                                 validators=[validators.MinLengthValidator(MIN_LINE_NAME_LENGTH)])

    def __str__(self):
        return self.line_name


class Line_details(models.Model):
    class Meta:
        ordering = ['address_line']

    material_line = models.CharField(max_length=9, unique=False)
    address_line = models.CharField(max_length=15)
    line_name = models.ForeignKey(Production_line, on_delete=models.RESTRICT, null=True, blank=True)
    transporter_name = models.ForeignKey(TransportUser, on_delete=models.RESTRICT, null=True,
                                         blank=True)


    def get_line_name(self):
        return self.line_name.line_name

    def get_transporter_name(self):
        return self.transporter_name


class Warehouse(models.Model):
    class Meta:
        ordering = ['address_warehouse']

    material_warehouse = models.CharField(max_length=9, unique=True)
    address_warehouse = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.material_warehouse
