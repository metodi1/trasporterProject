from transporterProject.common.models import Production_line


def get_production_lines():

    try:
        return Production_line.objects.all()
    except Production_line.DoesNotExist:
        return None