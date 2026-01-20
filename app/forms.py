from django.forms import ModelForm
from .models import Clientes

class ClientesForm(ModelForm):
    class Meta:
        model = Clientes
        exclude = ['estado, documento']

# class ProductosForm(ModelForm):
#     class Meta:
#         model = Productos
#         fields = "__all__"