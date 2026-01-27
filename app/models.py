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
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, blank=True)
    rol = models.ForeignKey(Roles, on_delete=models.PROTECT)
    estado = models.CharField(max_length=10,choices=ESTADOS,default='activo')
    password = models.CharField(max_length=100, default='')
    ultimo_acceso = models.DateTimeField(null=True, blank=True)
    fecha_ingreso = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.nombre} ({self.rol.nombre})"
    
    def save(self, *args, **kwargs):
        if self.correo:
            self.correo = self.correo.lower()
        super().save(*args, **kwargs)

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
    estado = models.CharField(max_length=10, choices=ESTADOS, default='activo')
    password = models.CharField(max_length=100, default='')
    fecha_registro = models.DateTimeField(auto_now_add=True)
    rol = models.ForeignKey(Roles, on_delete=models.PROTECT, default=1)


    def __str__(self):
        return self.nombre
    
    def save(self, *args, **kwargs):
        if self.correo:
            self.correo = self.correo.lower()
        super().save(*args, **kwargs)

# ----- CATEGORÍAS -----
class Categorias(models.Model):
    nombre = models.CharField(max_length=50)
    descripción = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre
    
class Productos(models.Model):
    categoria = models.ForeignKey(Categorias, on_delete=models.PROTECT, related_name='productos' )

    nombre = models.CharField(max_length=200)

    descripcion = models.TextField(blank=True)

    precio = models.DecimalField(max_digits=10, decimal_places=2)

    stock = models.PositiveIntegerField(default=0)

    fecha_vencimiento = models.DateField(blank=True, null=True)

    requiere_receta = models.BooleanField(default=False)

    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)

    activo = models.BooleanField(default=True)

    creado = models.DateTimeField(auto_now_add=True)

    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

    # 🔹 helpers útiles
    def disponible(self):
        return self.stock > 0 and self.activo


class Pedido(models.Model):

    ESTADOS = (
        ('pendiente', 'Pendiente'),
        ('listo', 'Listo'),
        ('enviado', 'Enviado'),
        ('entregado', 'Entregado'),
        ('cancelado', 'Cancelado'),
    )

    cliente = models.ForeignKey(Clientes, on_delete=models.PROTECT, related_name='pedidos')

    estado = models.CharField(max_length=20, choices=ESTADOS, default='pendiente')

    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    fecha_pedido = models.DateTimeField(default=timezone.now)

    direccion_envio = models.CharField(max_length=300)

    notas = models.TextField(blank=True)

    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"
        ordering = ['-fecha_pedido']

    def __str__(self):
        return f"Pedido #{self.id} - {self.cliente.nombre}"

    def calcular_total(self):
        total = sum(
            item.subtotal() for item in self.detalles.all()
        )
        self.total = total
        self.save()

class ProductoPedido(models.Model):

    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='detalles')

    producto = models.ForeignKey(Productos, on_delete=models.PROTECT)

    cantidad = models.PositiveIntegerField(default=1)

    precio = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "Detalle del pedido"
        verbose_name_plural = "Detalles del pedido"

    def __str__(self):
        return f"{self.producto.nombre} x {self.cantidad}"

    def subtotal(self):
        return self.precio * self.cantidad
