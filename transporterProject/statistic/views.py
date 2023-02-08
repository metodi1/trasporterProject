from datetime import datetime

from dateutil.utils import today
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.generic import DetailView, ListView, TemplateView

from transporterProject.core.filters import data_orders_statistic
from transporterProject.core.my_objects import Transporter_statistic_closed
from transporterProject.statistic.models import TransportersLikes
from transporterProject.tasks.models import Task


# Create your views  STATSISTIC

def ChartTransporter(request):
    open_orders_table, closed_orders_table = data_orders_statistic('transporter')

    context = {
        'open_orders_table': open_orders_table,
        'closed_orders_table': closed_orders_table,

    }
    return render(request, 'statistic/Statistics Transporters.html', context)


def ChartLine(request):
    what = 'line'
    statistic_name = 'Total orders by lines'
    data_for_print = []
    if request.POST.get('line'):
        what = 'line'
        statistic_name = 'Orders by lines'

    if request.POST.get('transporter'):
        what = 'transporter_close_task'
        statistic_name = 'Total orders by transporter'

    if request.POST.get('end_date'):
        what = 'end_date'
        statistic_name = 'Total orders by end date'


    if request.POST.get('button-like'):
        done = request.POST.get('button-like')
        t = TransportersLikes.objects.filter(transporter=done, liker_today=request.user, date_of_like=today().date())

        if not t:
            TransportersLikes.objects.create(
                transporter=done,
                liker_today=request.user,
                )
        else:
            t.delete()


    open_orders_table, closed_orders_table = data_orders_statistic(what)
    transporter_open_orders, transporter_closed_orders = data_orders_statistic('transporter_close_task')

    for transporter in transporter_closed_orders:
        liker_list = []
        for_print_obj = Transporter_statistic_closed()

        for_print_obj.today_closed_orders = Task.objects.filter(transporter_close_task=transporter,
                                                                status_line=True, status_warehouse=True,
                                                                end_date=datetime.today()).count()
        for_print_obj.total_closed_orders = Task.objects.filter(transporter_close_task=transporter,
                                                                status_line=True, status_warehouse=True,
                                                                ).count()

        for_print_obj.today_likes = TransportersLikes.objects.filter(transporter=transporter,
                                                                     date_of_like=datetime.today()).count()
        for_print_obj.total_likes = TransportersLikes.objects.filter(transporter=transporter).count()

        for ttt in TransportersLikes.objects.all():
            if ttt.transporter == transporter:
                liker_list.append(ttt.liker_today)
                if ttt.liker_today == request.user.username and ttt.date_of_like == today().date():
                    for_print_obj.curren_user_like = True

        for_print_obj.likers = liker_list
        for_print_obj.transporter = transporter
        data_for_print.append(for_print_obj)

    context = {
        'open_orders_table': open_orders_table,
        'closed_orders_table': closed_orders_table,
        'what': what,
        'statistic_name': statistic_name,
        'data_for_print': data_for_print,
    }

    return render(request, 'statistic/Statistics.html', context)


def user_liked_transporter(request, liker):
    print(liker)
