from django.shortcuts import render, redirect
from .forms import ClientesForm #, ProductosForm
from .models import Clientes
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

def login(req):
    if req.method == 'POST':
        correo = req.POST.get("correo", "").strip().lower()
        password = req.POST.get("password", "").strip()

        if not correo or not password:
            print('[DEBUG]: Completa el correo y la contraseña.')
            
            mensaje_error = "Completa el correo y la contraseña."
            return render(req, 'pages/auth/login.html', {'mensaje_error': mensaje_error})

        user = Clientes.objects.filter(correo=correo).first()

        if not user or not check_password(password, user.password):
            print('[DEBUG]: Correo o contraseña incorrectos')
            
            mensaje_error = "Correo o contraseña incorrectos."
            return render(req, 'pages/auth/login.html', {'mensaje_error': mensaje_error})

        req.session["id"] = user.id
        print('[DEBUG]: Usuario logeado con exito')
        messages.success(req, f"Bienvenido {user.nombre}")
        return redirect('inicio')
    else:
        mensaje_error = ''
        return render(req, 'pages/auth/login.html', {'mensaje_error': mensaje_error})



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


            if Clientes.objects.filter(correo=correo).exists():
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

# def sistema_productos(req):
#     productos = Productos.objects.all()
#     return render(req, 'pages/empleado/productos.html', {'productos': productos})

# def categorias(req):
#     return render(req, 'pages/empleado/categorias.html')

# def inventario(req):
#     if req.method=='POST':
#         productos_form = ProductosForm(req.POST)
#         if productos_form.is_valid():
#             productos_form.save()
#         else:
#             productos_form = ProductosForm()
#     return render(req, 'pages/empleado/inventario.html', {"productos_form":productos_form})