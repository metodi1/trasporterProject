from django.contrib import admin

from transporterProject.statistic.models import TransportersLikes
from transporterProject.tasks.models import Task


# Register your models here.
@admin.register(TransportersLikes)
class Task_detailsAdmin(admin.ModelAdmin):
    pass