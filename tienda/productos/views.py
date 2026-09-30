from django.shortcuts import render, redirect, get_object_or_404
# Se agregan Categoria y CategoriaForm a las importaciones
from .models import Producto, Categoria
from .forms import ProductoForm, CategoriaForm

# ==========================================
# VISTAS PARA PRODUCTOS
# ==========================================

def producto_list(request):
    productos = Producto.objects.all()
    return render(request, 'productos/listado.html', {'productos': productos})

def producto_new(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('producto_list')
    else:
        form = ProductoForm()
    return render(request, 'productos/registro.html', {'form': form, 'titulo': 'Registrar Producto'})

def producto_detail(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, 'productos/detalle.html', {'producto': producto})

def producto_edit(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == "POST":
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('producto_list')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'productos/registro.html', {'form': form, 'titulo': 'Editar Producto'})

def producto_delete(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == "POST":
        producto.delete()
        return redirect('producto_list')
    return render(request, 'productos/eliminar.html', {'producto': producto})


# ==========================================
# NUEVAS VISTAS PARA CATEGORÍAS
# ==========================================

def categoria_list(request):
    categorias = Categoria.objects.all()
    return render(request, 'categorias/listado.html', {'categorias': categorias})

def categoria_new(request):
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categoria_list')
    else:
        form = CategoriaForm()
    return render(request, 'categorias/registro.html', {'form': form, 'titulo': 'Registrar Categoría'})

def categoria_edit(request, pk):
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
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == "POST":
        categoria.delete()
        return redirect('categoria_list')
    return render(request, 'categorias/eliminar.html', {'categoria': categoria})