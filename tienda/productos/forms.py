from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'categoria', 'precio', 'cantidad']
        labels = {
            'nombre': 'Nombre del Producto',
            'categoria': 'Categoría',
            'precio': 'Precio ($)',
            'cantidad': 'Cantidad Disponible',
        }
        