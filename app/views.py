from django.shortcuts import render
from .forms import ClientesForm
# Pantallas del CLIENTE
def inicio(req):
    return render(req,'pages/cliente/inicio.html')

def productos(req):
    return render(req,'pages/cliente/productos.html')

def contacto(req):
    return render(req,'pages/cliente/contacto.html')

# Pantallas de AUTENTIFICACION
def login(req):
    return render(req,'pages/auth/login.html')

def register(req):
    if req.method == 'POST':
        print("[DEBUG]: El método es post")
        form = ClientesForm(req.POST)
        if form.is_valid():
            print("[DEBUG]: El formulario es válido")
            form.save()
        else:
            print("[DEBUG]: ", form.errors)
    else:
        form = ClientesForm()  # Formulario vacío para GET

    return render(req, 'pages/auth/register.html', {'form': form})