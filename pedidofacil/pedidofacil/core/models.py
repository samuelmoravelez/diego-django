from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

class Producto(models.Model):
    nombre = models.CharField(max_length=150, verbose_name="Nombre del Producto")
    descripcion = models.TextField(max_length=500, verbose_name="Descripción")
    precio = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        validators=[MinValueValidator(0.01)],
        verbose_name="Precio"
    )
    cantidad_disponible = models.IntegerField(
        validators=[MinValueValidator(0)],
        verbose_name="Cantidad Disponible"
    )
    fecha_registro = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Registro")

    class Meta:
        ordering = ['-fecha_registro']

    def __str__(self):
        return f"{self.nombre} (${self.precio})"


class Pedido(models.Model):
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('confirmado', 'Confirmado'),
        ('cancelado', 'Cancelado'),
    ]

    numero_pedido = models.CharField(
        max_length=50, 
        unique=True, 
        verbose_name="Número de Pedido"
    )
    cliente = models.CharField(max_length=150, verbose_name="Nombre del Cliente")
    fecha_registro = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Registro")
    descripcion = models.TextField(verbose_name="Descripción del Pedido")
    valor_total = models.DecimalField(
        max_digits=12, 
        decimal_places=2, 
        validators=[MinValueValidator(0.01)],
        verbose_name="Valor Total"
    )
    estado = models.CharField(
        max_length=20, 
        choices=ESTADO_CHOICES, 
        default='pendiente',
        verbose_name="Estado"
    )
    usuario = models.ForeignKey(
        User, 
        on_delete=models.PROTECT, 
        related_name="pedidos",
        verbose_name="Usuario que Registró"
    )

    class Meta:
        ordering = ['-fecha_registro']

    def __str__(self):
        return f"Pedido #{self.numero_pedido} - {self.cliente}"