from django.urls import path
from . import views

urlpatterns = [
    # Rutas para Productos
    path('', views.producto_list, name='producto_list'),
    path('productos/nuevo/', views.producto_new, name='producto_new'),
    path('productos/<int:pk>/', views.producto_detail, name='producto_detail'),
    path('productos/<int:pk>/editar/', views.producto_edit, name='producto_edit'),
    path('productos/<int:pk>/eliminar/', views.producto_delete, name='producto_delete'),

    # Rutas para Categorías
    path('categorias/', views.categoria_list, name='categoria_list'),
    path('categorias/nueva/', views.categoria_new, name='categoria_new'),
    path('categorias/<int:pk>/editar/', views.categoria_edit, name='categoria_edit'),
    path('categorias/<int:pk>/eliminar/', views.categoria_delete, name='categoria_delete'),
]