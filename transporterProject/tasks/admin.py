from django.contrib import admin

from transporterProject.tasks.models import Task


# Register your models here.
@admin.register(Task)
class Task_detailsAdmin(admin.ModelAdmin):
    list_display = ['s_number']