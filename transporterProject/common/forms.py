# common forms

from django import forms
from django.forms import CheckboxInput
from django.http import request

from transporterProject.accounts.models import TransportUser
from transporterProject.common.models import Production_line, Warehouse, Line_details

line_name = Production_line.objects.values_list('line_name')


class Chouse_line_form(forms.ModelForm):
    class Meta:
        model = Production_line
        fields = ['line_name']
        widgets = {
            'line_name': CheckboxInput(),
        }


class Add_Warehouse_address(forms.ModelForm):
    class Meta:
        model = Warehouse
        fields = ["material_warehouse", "address_warehouse"]
        labels = {
            'material_warehouse': 'Material',
            'address_warehouse': 'Address in warehouse',
        }
        label_suffix = {
            'material_warehouse': 'Сканирай баркода на етикета',
        }


class Add_Lines(forms.ModelForm):
    class Meta:
        model = Production_line
        fields = ["line_name"]
        labels = {
            'line_name': 'Име на линия',
        }
        label_suffix = {
            'line_name': 'Напиште името на линията',
        }


class Material_production_line_positions(forms.ModelForm):
    class Meta:
        model = Line_details
        fields = ["material_line", "address_line", "line_name", "transporter_name"]
