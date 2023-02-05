from django.urls import path, include

from transporterProject.statistic.views import ChartTransporter, ChartLine, user_liked_transporter

urlpatterns = (

    path('t/', ChartTransporter, name='statistic transporter'),
    path('line', ChartLine, name='statistic line'),
    path('likes', user_liked_transporter, name='likes'),
)
