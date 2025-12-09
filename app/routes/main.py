from django.urls import path, include
from app import views
urlpatterns = [
    # Pantallas de CLIENTE
    path('',views.inicio, name='inicio'),
    path('/productos',views.productos, name='productos'),

    # Pantallas de AUTENTIFICACION
    path('/login',views.login, name='login'),
    path('/register',views.render, name='register')
]