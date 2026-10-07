"""
Enrutamiento raíz del proyecto tienda.

Monta el panel de administración de Django y delega las rutas públicas
en la aplicación productos.
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Panel de administración integrado de Django
    path('admin/', admin.site.urls),
    # CRUD de productos y categorías bajo la raíz del sitio
    path('', include('productos.urls')),
]
