"""
Modelos de datos de la aplicación productos.

Define las entidades Categoria y Producto y la relación entre ellas.
"""

from django.db import models


class Categoria(models.Model):
    """
    Categoría de clasificación para productos del inventario.

    Attributes:
        nombre (str): Nombre identificador de la categoría.
        descripcion (str | None): Texto opcional con detalle de la categoría.
    """

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        """
        Representación legible de la categoría.

        Returns:
            str: Nombre de la categoría.
        """
        return self.nombre


class Producto(models.Model):
    """
    Producto registrado en la tienda con precio, stock y estado.

    Attributes:
        nombre (str): Nombre del producto.
        categoria (Categoria): Categoría a la que pertenece (FK).
        precio (Decimal): Precio unitario con dos decimales.
        cantidad (int): Unidades disponibles en inventario.
        estado (bool): True si está activo; False si está inactivo.
    """

    nombre = models.CharField(max_length=100)
    # Relación muchos-a-uno: al borrar la categoría se eliminan sus productos (CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.IntegerField()
    # Bandera de disponibilidad en catálogo (valor por defecto: activo)
    estado = models.BooleanField(default=True)

    def __str__(self):
        """
        Representación legible del producto.

        Returns:
            str: Nombre del producto.
        """
        return self.nombre
