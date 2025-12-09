from django.urls import path, include
from app import views
urlpatterns = [
    path('',views.inicio, name='inicio'),
    path('',views.productos, name='productos'),
]