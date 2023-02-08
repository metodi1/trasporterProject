import datetime

from django.http import request, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils import timezone

from django.views.generic import View, ListView, DetailView, FormView, TemplateView
from django.views.generic.edit import ModelFormMixin, UpdateView, DeleteView

from transporterProject.common.forms import Add_Warehouse_address, Material_production_line_positions, \
    Add_Lines
from transporterProject.common.models import Warehouse, Line_details, Production_line
from transporterProject.statistic.views import ChartTransporter, ChartLine
from transporterProject.tasks.models import Task


# Create your views here.


def Home_page(request):
    if request.user.is_authenticated:
        return ChartLine(request)
    else:
        return render(request, 'pages/Home page.html')


class Warehouse_page_View(ListView, ModelFormMixin):
    # specify the model to use
    model = Warehouse
    form_class = Add_Warehouse_address
    template_name = 'pages/Warehouse.html'

    def get(self, request, *args, **kwargs):
        self.object = None
        self.form = self.form_class
        # Explicitly states what get to call:
        return ListView.get(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        # When the form is submitted, it will enter here
        self.object = None
        self.form = self.get_form(self.form_class)

        if self.form.is_valid():
            self.object = self.form.save()
            self.form = self.form
            # Here ou may consider creating a new instance of form_class(),
            # so that the form will come clean.

        # Whether the form validates or not, the view will be rendered by get()
        return self.get(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        # Just include the form
        context = super(Warehouse_page_View, self).get_context_data(*args, **kwargs)
        context['form'] = self.form
        return context


class Warehouse_Edit_View(UpdateView):
    template_name = 'pages/Warehouse Edit.html'
    model = Warehouse
    fields = ('material_warehouse', 'address_warehouse')

    def get_success_url(self):
        return reverse_lazy('warehouse page')


class Warehouse_Delete_view(DeleteView):
    template_name = 'pages/Warehouse Delete.html'
    model = Warehouse
    success_url = reverse_lazy('warehouse page')


class Production_line_catalog(ListView, ModelFormMixin):
    model = Production_line
    form_class = Add_Lines
    template_name = 'pages/Lines catalog.html'

    def get(self, request, *args, **kwargs):
        self.object = None
        self.form = self.form_class
        # Explicitly states what get to call:
        return ListView.get(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        # When the form is submitted, it will enter here
        self.object = None
        self.form = self.get_form(self.form_class)

        if self.form.is_valid():
            self.object = self.form.save()
            self.form = self.form
            # Here ou may consider creating a new instance of form_class(),
            # so that the form will come clean.

        # Whether the form validates or not, the view will be rendered by get()
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)

        contex['form'] = self.form

        return contex


class Production_line_catalog_edit(UpdateView):
    template_name = 'pages/Lines catalog Edit.html'
    model = Production_line
    fields = ('line_name',)

    def get_success_url(self):
        return reverse_lazy('lines catalog')


class Production_line_catalog_delete(DeleteView):
    template_name = 'pages/Lines catalog Delete.html'
    model = Production_line
    success_url = reverse_lazy('lines catalog')


def Production_Line_View(request, pk):
    get_line_name = Production_line.objects.get(id=pk)
    materials = Line_details.objects.filter(line_name=get_line_name)
    line_materials = []
    for material in materials:
        line_materials.append(material)

    if request.method == 'GET':
        form = Material_production_line_positions()

    if request.method == "POST":
        form = Material_production_line_positions(request.POST)
        if form.is_valid():
            material_position = form.save(commit=False)
            material_position.line_name = get_line_name
            material_position.transporter_name = request.user
            material_position.save()
            form = form
            return redirect(request.META['HTTP_REFERER'])

    context = {
        'line_materials': line_materials,
        'get_line_name': get_line_name,
        'form': form,
    }

    return render(request, 'pages/Production line.html', context)


class Production_Line_Edit_View(UpdateView):
    template_name = 'pages/Production line Edit.html'
    model = Line_details
    fields = ('material_line', 'address_line')

    def get_success_url(self):
        return reverse_lazy('lines catalog')


class Production_Line_Delete_View(DeleteView):
    template_name = 'pages/Production line Delete.html'
    model = Line_details
    success_url = reverse_lazy('lines catalog')
