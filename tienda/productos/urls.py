"""
Rutas URL de la aplicación productos.

Asocia cada path con una vista del CRUD de productos y categorías.
Incluidas desde tienda.urls con path('', include('productos.urls')).
"""

from django.urls import path
from . import views

urlpatterns = [
    # --- Productos (Read: listado en la raíz del sitio) ---
    path('', views.producto_list, name='producto_list'),
    # Create
    path('productos/nuevo/', views.producto_new, name='producto_new'),
    # Read (detalle por pk)
    path('productos/<int:pk>/', views.producto_detail, name='producto_detail'),
    # Update
    path('productos/<int:pk>/editar/', views.producto_edit, name='producto_edit'),
    # Delete (confirmación GET + borrado POST)
    path('productos/<int:pk>/eliminar/', views.producto_delete, name='producto_delete'),

    # --- Categorías ---
    path('categorias/', views.categoria_list, name='categoria_list'),
    path('categorias/nueva/', views.categoria_new, name='categoria_new'),
    path('categorias/<int:pk>/editar/', views.categoria_edit, name='categoria_edit'),
    path('categorias/<int:pk>/eliminar/', views.categoria_delete, name='categoria_delete'),
]
