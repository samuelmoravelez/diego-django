from django import forms
from .models import Asistencia

class AsistenciaForm(forms.ModelForm):
    class Meta:
        model = Asistencia
        fields = '__all__' # Incluye todos los campos del modelo
        # Este widget es para que el campo de fecha muestre un calendario en el navegador
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
        }