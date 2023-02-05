from django.db import models


# Create your models here.

class Task(models.Model):
    class Meta:
        ordering = ['id']

    s_number = models.CharField(max_length=9)
    transporter = models.CharField(max_length=30)
    line = models.CharField(max_length=30)
    status_line = models.BooleanField(default=False)
    status_warehouse = models.BooleanField(default=False)
    start_time = models.TimeField(auto_now_add=True)
    end_time = models.TimeField(auto_now=True)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(auto_now=True)
