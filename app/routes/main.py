from django.urls import path, include
from app import views
urlpatterns = [
    # Pantallas de CLIENTE
    path('',views.inicio, name='inicio'),
    path('productos/',views.productos, name='productos'),
    path('contacto/',views.productos, name='contacto'),

    # Pantallas de AUTENTIFICACION
    path('login/',views.login, name='login'),
    path('register/',views.register, name='register'),

    # Pantallas de EMPLEADO
    path('sistema/dashboard/', views.dashboard, name='dashboard'),
    path('sistema/pedidos/', views.pedidos, name='pedidos'),
    path('sistema/inventario/', views.inventario, name='inventario'),
    path('sistema/clientes/', views.clientes, name='clientes'),
    path('sistema/empleados/', views.empleados, name='empleados'),
]