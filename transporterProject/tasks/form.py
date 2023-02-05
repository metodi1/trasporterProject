from django import forms

from transporterProject.tasks.models import Task


############
# task forms

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["s_number"]

