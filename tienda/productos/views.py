"""
Vistas HTTP del CRUD de productos y categorías.

Cada función consulta o persiste modelos, usa formularios y renderiza plantillas.
"""

from django.shortcuts import render, redirect, get_object_or_404
# Se agregan Categoria y CategoriaForm a las importaciones
from .models import Producto, Categoria
from .forms import ProductoForm, CategoriaForm

# ==========================================
# VISTAS PARA PRODUCTOS
# ==========================================


def producto_list(request):
    """
    Lista todos los productos registrados.

    Args:
        request (HttpRequest): Petición entrante.

    Returns:
        HttpResponse: Plantilla listado.html con el queryset de productos.
    """
    # Consulta ORM: recupera todos los registros de Producto
    productos = Producto.objects.all()
    return render(request, 'productos/listado.html', {'productos': productos})


def producto_new(request):
    """
    Crea un producto nuevo mediante ProductoForm.

    Args:
        request (HttpRequest): Petición GET (formulario vacío) o POST (datos).

    Returns:
        HttpResponse: Redirección al listado si guarda; formulario en caso contrario.
    """
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            # Persiste el producto en la base de datos
            form.save()
            return redirect('producto_list')
    else:
        form = ProductoForm()
    return render(request, 'productos/registro.html', {'form': form, 'titulo': 'Registrar Producto'})


def producto_detail(request, pk):
    """
    Muestra el detalle de un producto por clave primaria.

    Args:
        request (HttpRequest): Petición entrante.
        pk (int): Identificador del producto.

    Returns:
        HttpResponse: Plantilla detalle.html con la instancia encontrada.
    """
    # 404 si no existe el pk solicitado
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, 'productos/detalle.html', {'producto': producto})


def producto_edit(request, pk):
    """
    Actualiza un producto existente.

    Args:
        request (HttpRequest): Petición GET o POST con datos del formulario.
        pk (int): Identificador del producto a editar.

    Returns:
        HttpResponse: Redirección al listado tras guardar o formulario con instance.
    """
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == "POST":
        # instance enlaza el formulario con el registro existente en BD
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('producto_list')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'productos/registro.html', {'form': form, 'titulo': 'Editar Producto'})


def producto_delete(request, pk):
    """
    Elimina un producto tras confirmación POST.

    Args:
        request (HttpRequest): GET muestra confirmación; POST ejecuta borrado.
        pk (int): Identificador del producto.

    Returns:
        HttpResponse: Redirección al listado o plantilla eliminar.html.
    """
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == "POST":
        producto.delete()
        return redirect('producto_list')
    return render(request, 'productos/eliminar.html', {'producto': producto})


# ==========================================
# NUEVAS VISTAS PARA CATEGORÍAS
# ==========================================


def categoria_list(request):
    """
    Lista todas las categorías registradas.

    Args:
        request (HttpRequest): Petición entrante.

    Returns:
        HttpResponse: Plantilla categorias/listado.html con el queryset.
    """
    categorias = Categoria.objects.all()
    return render(request, 'categorias/listado.html', {'categorias': categorias})


def categoria_new(request):
    """
    Crea una categoría nueva mediante CategoriaForm.

    Args:
        request (HttpRequest): Petición GET o POST.

    Returns:
        HttpResponse: Redirección a categoria_list si guarda; formulario si no.
    """
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categoria_list')
    else:
        form = CategoriaForm()
    return render(request, 'categorias/registro.html', {'form': form, 'titulo': 'Registrar Categoría'})


def categoria_edit(request, pk):
    """
    Actualiza una categoría existente.

    Args:
        request (HttpRequest): Petición GET o POST.
        pk (int): Identificador de la categoría.

    Returns:
        HttpResponse: Redirección al listado de categorías o formulario de edición.
    """
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == "POST":
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('categoria_list')
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'categorias/registro.html', {'form': form, 'titulo': 'Editar Categoría'})


def categoria_delete(request, pk):
    """
    Elimina una categoría tras confirmación POST.

    Por CASCADE en Producto.categoria, también borra productos vinculados.

    Args:
        request (HttpRequest): GET confirma; POST elimina.
        pk (int): Identificador de la categoría.

    Returns:
        HttpResponse: Redirección a categoria_list o plantilla de confirmación.
    """
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == "POST":
        # El borrado en cascada afecta productos con esta FK
        categoria.delete()
        return redirect('categoria_list')
    return render(request, 'categorias/eliminar.html', {'categoria': categoria})
