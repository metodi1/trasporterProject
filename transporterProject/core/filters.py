from transporterProject.common.models import Line_details
from transporterProject.tasks.models import Task


def find_material_line_address(line_id, material):
    line_material_address = None
    all_line_materials = Line_details.objects.filter(line_name_id=line_id)
    # print(all_line_materials[0])
    for m in all_line_materials:
        if m.material_line == material:
            line_material_address = material.address_line

    return line_material_address


def data_orders_statistic(what_order):
    what = what_order
    all_orders = Task.objects.all()
    open_orders_table = {}
    closed_orders_table = {}

    for single_order in all_orders:
        if single_order.__getattribute__(what) not in open_orders_table:
            open_orders_table[single_order.__getattribute__(what)] = 0
            closed_orders_table[single_order.__getattribute__(what)] = 0

    labels = []
    for single_order in all_orders:
        if single_order.status_line != True and single_order.status_warehouse != True:
            if single_order.__getattribute__(what) not in open_orders_table:
                open_orders_table[single_order.__getattribute__(what)] = 1
            else:
                open_orders_table[single_order.__getattribute__(what)] += 1
        else:
            if single_order.__getattribute__(what) not in closed_orders_table:
                closed_orders_table[single_order.__getattribute__(what)] = 1
            else:
                closed_orders_table[single_order.__getattribute__(what)] += 1

    for x in open_orders_table.keys():
        labels.append(x)

    for x in closed_orders_table.keys():
        labels.append(x)

        # insert the list to the set
        list_set = set(labels)
        # convert the set to the list
        unique_list = (list(list_set))

    return open_orders_table, closed_orders_table



