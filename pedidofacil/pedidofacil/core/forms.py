from django import forms
from .models import Producto, Pedido

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'cantidad_disponible']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'id': 'id_nombre'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'id': 'id_descripcion'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'id': 'id_precio'}),
            'cantidad_disponible': forms.NumberInput(attrs={'class': 'form-control', 'id': 'id_cantidad_disponible'}),
        }

    def clean_precio(self):
        precio = self.cleaned_data.get('precio')
        if precio is not None and precio <= 0:
            raise forms.ValidationError("El precio debe ser un número mayor que cero.")
        return precio

    def clean_cantidad_disponible(self):
        cantidad = self.cleaned_data.get('cantidad_disponible')
        if cantidad is not None and cantidad < 0:
            raise forms.ValidationError("La cantidad disponible no puede ser negativa.")
        return cantidad


class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['numero_pedido', 'cliente', 'descripcion', 'valor_total', 'estado']
        widgets = {
            'numero_pedido': forms.TextInput(attrs={'class': 'form-control', 'id': 'id_numero_pedido'}),
            'cliente': forms.TextInput(attrs={'class': 'form-control', 'id': 'id_cliente'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'id': 'id_descripcion'}),
            'valor_total': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'id': 'id_valor_total'}),
            'estado': forms.Select(attrs={'class': 'form-select', 'id': 'id_estado'}),
        }

    def clean_valor_total(self):
        valor = self.cleaned_data.get('valor_total')
        if valor is not None and valor <= 0:
            raise forms.ValidationError("El valor total debe ser un número mayor que cero.")
        return valor