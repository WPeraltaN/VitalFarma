from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Clientes(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    password = models.CharField(max_length=200)
    def __str__(self):
        return self.nombre
    

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    descripción = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre


class Productos(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    descripcion = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    fecha_vencimiento = models.DateField()
    imagen = models.CharField(max_length=200)
    def __str__(self):
        return self.nombre
    

