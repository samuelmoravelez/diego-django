from django.contrib import admin
from .models import Asistencia

@admin.register(Asistencia)
class AsistenciaAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellidos', 'documento', 'fecha', 'asistio')
    list_filter = ('asistio', 'fecha', 'tipo_documento')
    search_fields = ('documento', 'nombres', 'apellidos')