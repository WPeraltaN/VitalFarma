from django.shortcuts import render, redirect
from .forms import ClientesForm
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
    if req.user.is_authenticated: # Condicional si el usuario esta autentificado
        return redirect('pages/cliente/inicio.html')
    if req.method == 'POST':
        email = req.POST.get("email", "").strip().lower()
        password = req.POST.get("password", "").strip().lower()
        
        if not email or not password:
            messages.error(req, "Completa el correo y contrasena.")
            return render(req, 'pages/auth/login.html')
        user = authenticate(req, username=email, password=password) #Funcion autentificar la cual se le estara enviando los parametros username y password los cuales se almacenarn en la variable user
        
        if user is None:
            messages.error(req, "Correo o contrasena incorrectos.")
            return render(req, 'pages/auth/login.html')
        login(req,user)
        messages.success(req, 'Bienvenido', {user.email})
        return redirect('pages/cliente/inicio.html')        
    return render(req,'pages/auth/login.html')

def register(req):
    if req.method == 'POST':
        form = ClientesForm(req.POST)
        if form.is_valid():
            print("[DEBUG]: El formulario es válido")
            form.save()
        else:
            error = form.errors
            print("[DEBUG]: ", form.errors)
    else:
        form = ClientesForm()  # Formulario vacío para GET

    return render(req, 'pages/auth/register.html', {'form': form})



#-------------------------------------------------
# Pantallas de EMPLEADO
#-------------------------------------------------
def dashboard(req):
    return render(req, 'pages/empleado/dashboard.html')

def productos(req):
    return render(req, 'pages/empleado/productos.html')

def categorias(req):
    return render(req, 'pages/empleado/categorias.html')