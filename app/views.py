from django.shortcuts import render

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
    return render(req,'pages/auth/register.html')