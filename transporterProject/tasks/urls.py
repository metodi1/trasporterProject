from django.urls import path

from transporterProject.tasks.views import Task_view

urlpatterns = (
    path('', Task_view, name='task page'),
)