"""CRUD de funcionários.

O PermissionRequiredMixin manda quem não entrou para o login e devolve 403 para quem
entrou mas não tem a permissão.
"""

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import EmployeeForm
from .models import Employee


class EmployeeListView(PermissionRequiredMixin, ListView):
    model = Employee
    permission_required = 'person.view_employee'


class EmployeeCreateView(PermissionRequiredMixin, CreateView):
    model = Employee
    form_class = EmployeeForm
    permission_required = 'person.add_employee'
    success_url = reverse_lazy('person:employee_list')


class EmployeeUpdateView(PermissionRequiredMixin, UpdateView):
    model = Employee
    form_class = EmployeeForm
    permission_required = 'person.change_employee'
    success_url = reverse_lazy('person:employee_list')

class EmployeeDeleteView(PermissionRequiredMixin, DeleteView):
    model = Employee
    permission_required = 'person.delete_employee'
    success_url = reverse_lazy('person:employee_list')
