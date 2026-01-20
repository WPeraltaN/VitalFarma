from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# ----- ROLES -----
class Roles(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField(blank=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

# ----- EMPLEADOS -----
class Empleados(models.Model):
    ESTADOS = (
        ('activo', 'Activo'),
        ('inactivo', 'Inactivo'),
        ('suspendido', 'Suspendido'),
    )

    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, blank=True)

    rol = models.ForeignKey(
        Roles,
        on_delete=models.PROTECT,
        related_name='empleados'
    )

    estado = models.CharField(
        max_length=10,
        choices=ESTADOS,
        default='activo'
    )

    en_turno = models.BooleanField(default=False)
    ultimo_acceso = models.DateTimeField(null=True, blank=True)
    fecha_ingreso = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.nombre} ({self.rol.nombre})"

# ----- CLIENTES -----
class Clientes(models.Model):
    ESTADOS = (
        ('activo', 'Activo'),
        ('inactivo', 'Inactivo'),
    )

    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, blank=True)
    documento = models.CharField(max_length=20, blank=True)

    direccion = models.CharField(max_length=300, default='')
    estado = models.CharField(
        max_length=10,
        choices=ESTADOS,
        default='activo'
    )
    password = models.CharField(max_length=100, default='')
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

# ----- CATEGORÍAS -----
class Categorias(models.Model):
    nombre = models.CharField(max_length=50)
    descripción = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre