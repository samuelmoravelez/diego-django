from django import forms
from .models import Producto, Categoria

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__' # Esto incluirá automáticamente el nuevo campo 'estado'