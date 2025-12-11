from django.forms import ModelForm
from .models import Clientes

class ClientesForm(ModelForm):
    class Meta:
        model = Clientes
        fields = "__all__"

