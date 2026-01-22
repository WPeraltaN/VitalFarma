from django.forms import ModelForm
from .models import Clientes, Empleados

class ClientesForm(ModelForm):
    class Meta:
        model = Clientes
        exclude = ['estado','documento','rol']

class EmpleadosForm(ModelForm):
    class Meta:
        model = Empleados
        exclude = ['ultimo_acceso', 'fecha_ingreso']