"""
Formularios ModelForm para crear y editar categorías y productos.

Vinculan los campos del modelo con la capa de presentación en las vistas.
"""

from django import forms
from .models import Producto, Categoria


class CategoriaForm(forms.ModelForm):
    """
    Formulario basado en el modelo Categoria para altas y ediciones.

    Meta:
        model: Categoria.
        fields: Todos los campos del modelo (nombre, descripcion).
    """

    class Meta:
        # Mapeo directo a la tabla Categoria en SQLite
        model = Categoria
        fields = '__all__'


class ProductoForm(forms.ModelForm):
    """
    Formulario basado en el modelo Producto para altas y ediciones.

    Meta:
        model: Producto.
        fields: Todos los campos del modelo, incluido estado y categoría (FK).
    """

    class Meta:
        # Incluye categoria como ModelChoiceField hacia registros de Categoria
        model = Producto
        fields = '__all__' # Esto incluirá automáticamente el nuevo campo 'estado'
