from django.shortcuts import render, redirect
from django.views import View

from transporterProject.common.models import Production_line, Line_details, Warehouse
from transporterProject.core.my_objects import Single_Task_details_obj
from transporterProject.tasks.form import TaskForm
from transporterProject.tasks.models import Task


#################
# task view


def Task_view(request, pk):
    get_line_name = Production_line.objects.get(id=pk)
    transporter_name = request.user.username
    tasks_list = []

    if request.method == 'GET':
        form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form_task = form.save(commit=False)
            form_task.transporter_open_task = request.user
            form_task.line = get_line_name.line_name
            form_task.save()
            form = form
            return redirect(request.META['HTTP_REFERER'])

    all_tasks = Task.objects.filter(line=get_line_name).all()

    for task in all_tasks:
        if (task.status_line == False or task.status_warehouse == False):
            material = task.s_number
            try:
                line_address = None
                all_line_materials = Line_details.objects.filter(line_name=get_line_name)
                for m in all_line_materials:
                    if m.material_line == material:
                        line_address = m.address_line

                # line_address = Line_details.objects.filter(material_line=material).get().address_line
            except:
                line_address = None
            try:
                warehouse_address = Warehouse.objects.filter(material_warehouse=material).get().address_warehouse
            except:
                warehouse_address = None

            single_task = Single_Task_details_obj()
            single_task.id = task.id
            single_task.s_number = material
            single_task.start_time = task.start_time
            single_task.warehouse_address = warehouse_address
            single_task.line_address = line_address
            single_task.status_warehouse = task.status_warehouse
            single_task.status_line = task.status_line
            tasks_list.append(single_task)

    contex = {
        'get_line_name': get_line_name,
        'transporter_name': transporter_name,
        'form': form,
        'tasks_list': tasks_list,
    }

    if request.method == "POST":
        done = request.POST.get('warehouse-done')

        if done:
            t = Task.objects.get(id=done)
            t.status_warehouse = True
            t.transporter_close_task = request.user
            t.save()
            return redirect(request.META['HTTP_REFERER'])

    if request.method == "POST":
        done1 = request.POST.get('done')
        if done1:
            t = Task.objects.get(id=done1)
            t.status_line = True
            t.transporter_close_task = request.user
            t.save()
            return redirect(request.META['HTTP_REFERER'])

    return render(request, 'Task/Task.html', contex)
