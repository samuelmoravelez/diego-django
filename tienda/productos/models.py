from django.db import models

# NUEVO: Modelo para Categoría
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

# ACTUALIZADO: Modelo de Producto
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    # Enlazamos el producto con la categoría real:
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.IntegerField()
    # NUEVO: Atributo de estado (True = Activo, False = Inactivo)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre