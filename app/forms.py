from django.forms import ModelForm
from .models import Clientes, Productos

class ClientesForm(ModelForm):
    class Meta:
        model = Clientes
        fields = "__all__"

class ProductosForm(ModelForm):
    class Meta:
        model = Productos
        fields = "__all__"