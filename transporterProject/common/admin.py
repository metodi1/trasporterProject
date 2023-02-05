from django.contrib import admin

from transporterProject.common.models import Warehouse, Line_details, Production_line


# Register your models here.


@admin.register(Line_details)
class Line_detailsAdmin(admin.ModelAdmin):
    list_display = ['material_line', 'address_line', 'line_name','transporter_name']


@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ['material_warehouse', 'address_warehouse']


@admin.register(Production_line)
class Production_lineAdmin(admin.ModelAdmin):
    list_display = ['line_name']
