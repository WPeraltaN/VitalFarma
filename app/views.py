from django.shortcuts import render, redirect
from .forms import ClientesForm, EmpleadosForm
from .models import Clientes, Empleados
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
# Pantallas del CLIENTE
#-------------------------------------------------
def inicio(req):
    return render(req,'pages/cliente/inicio.html')

def productos(req):
    return render(req,'pages/cliente/productos.html')

def contacto(req):
    return render(req,'pages/cliente/contacto.html')



#-------------------------------------------------
# Pantallas de AUTENTIFICACIÓN
#-------------------------------------------------

from django.contrib.auth.hashers import check_password

def login(req):
    if req.method == 'POST':
        correo = req.POST.get("correo", "").strip().lower()
        password = req.POST.get("password", "").strip()

        if not correo or not password:
            mensaje_error = "Completa el correo y la contraseña."
            return render(req, 'pages/auth/login.html', {'mensaje_error': mensaje_error})

        cliente = Clientes.objects.filter(correo=correo).first()
        if cliente and check_password(password, cliente.password):
            req.session["id"] = cliente.id
            messages.success(req, f"Bienvenido {cliente.nombre}")
            return redirect('inicio')

        empleado = Empleados.objects.filter(correo=correo).first()
        if empleado and check_password(password, empleado.password):
            req.session["id"] = empleado.id
            messages.success(req, f"Bienvenido {empleado.nombre}")
            return redirect('dashboard')

        mensaje_error = "Correo o contraseña incorrectos."
        return render(req, 'pages/auth/login.html', {'mensaje_error': mensaje_error})
    else:
        return render(req, 'pages/auth/login.html', {'mensaje_error': ''})



def register(req):
    if req.method == 'POST':
        form = ClientesForm(req.POST)
        if form.is_valid():
            print("[DEBUG]: El formulario es válido")
            
            password = req.POST.get('password')
            cpassword = req.POST.get('cpassword')
            correo = req.POST.get('correo', '').strip().lower()


            if password != cpassword:
                mensaje_error = 'Las contraseñas no coinciden'
                return render(req, 'pages/auth/register.html', {'form': form,'mensaje_error': mensaje_error})


            if Clientes.objects.filter(correo=correo).exists() or Empleados.objects.filter(correo=correo).exists():
                mensaje_error = 'Ya existe una cuenta con ese correo'
                return render(req, 'pages/auth/register.html', {'form': form,'mensaje_error': mensaje_error})

            cliente = form.save(commit=False)
            cliente.correo = correo
            cliente.password = make_password(password)
            cliente.save()

            messages.success(req, "Cuenta creada correctamente")
            return redirect('login')

        else:
            print("[DEBUG]: ", form.errors)
    else:
        form = ClientesForm()
        mensaje_error = ''
    return render(req, 'pages/auth/register.html', {'form': form, 'mensaje_error': mensaje_error})




#-------------------------------------------------
# Pantallas de EMPLEADO
#-------------------------------------------------
@login_required
def dashboard(req):
    return render(req, 'pages/empleado/dashboard.html')

def pedidos(req):
    return render(req, 'pages/empleado/pedidos.html')

def inventario(req):
    return render(req, 'pages/empleado/inventario.html')

def clientes(req):
    return render(req, 'pages/empleado/clientes.html')

def empleados(req):
    if req.method == 'POST':
        form = EmpleadosForm(req.POST)
        if form.is_valid():
            correo = req.POST.get('correo', '').strip().lower()
            password = req.POST.get('password')
            if Empleados.objects.filter(correo=correo).exists() or Clientes.objects.filter(correo=correo).exists():
                mensaje_error = 'Ya existe una cuenta con ese correo'
                return render(req, 'pages/empleado/empleados.html',{'form':form, 'mensaje_error':mensaje_error})
            
            empleado = form.save(commit=False)
            empleado.correo = correo
            empleado.password = make_password(password)
            empleado.save()
    else:
        form = EmpleadosForm()
        
    mensaje_error = ''
    return render(req, 'pages/empleado/empleados.html',{'form':form, 'mensaje_error':mensaje_error})
