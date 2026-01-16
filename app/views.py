from django.shortcuts import render, redirect
from .forms import ClientesForm
from .models import Productos, Clientes, Categoria
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
# Pantallas del CLIENTE
#-------------------------------------------------
def inicio(req):
    return render(req,'pages/cliente/inicio.html')

def productos(req):
    return render(req,'pages/cliente/productos.html')

def contacto(req):
    return render(req,'pages/cliente/contacto.html')



#-------------------------------------------------
# Pantallas de AUTENTIFICACION
#-------------------------------------------------

def login(req):
    if req.method == 'POST':
        correo = req.POST.get("correo", "").strip().lower()
        password = req.POST.get("password", "").strip()

        if not correo or not password:
            print('[DEBUG]: Completa el correo y la contraseña.')
            
            messages.error(req, "Completa el correo y la contraseña.")
            return render(req, 'pages/auth/login.html')

        user = Clientes.objects.filter(correo=correo).first()

        if not user or not check_password(password, user.password):
            print('[DEBUG]: Correo o contraseña incorrectos')
            
            messages.error(req, "Correo o contraseña incorrectos.")
            return render(req, 'pages/auth/login.html')

        req.session["id"] = user.id
        print('[DEBUG]: Usuario logeado con exito')
        messages.success(req, f"Bienvenido {user.nombre}")
        return redirect('inicio')

    return render(req, 'pages/auth/login.html')

from django.contrib.auth.hashers import make_password

def register(req):
    if req.method == 'POST':
        form = ClientesForm(req.POST)
        if form.is_valid():
            print("[DEBUG]: El formulario es válido")
            
            cliente = form.save(commit=False)
            cliente.password = make_password(form.cleaned_data['password'])
            cliente.save()

            messages.success(req, "Cuenta creada correctamente")
            return redirect('login')
        else:
            print("[DEBUG]: ", form.errors)
    else:
        form = ClientesForm()

    return render(req, 'pages/auth/register.html', {'form': form})




#-------------------------------------------------
# Pantallas de EMPLEADO
#-------------------------------------------------
@login_required
def dashboard(req):
    return render(req, 'pages/empleado/dashboard.html')

def sistema_productos(req):
    productos = Productos.objects.all()
    return render(req, 'pages/empleado/productos.html', {'productos': productos})

def categorias(req):
    return render(req, 'pages/empleado/categorias.html')