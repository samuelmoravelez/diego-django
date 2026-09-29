from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ProductoForm

# Vista para listar (ya la debes tener parecida)
def producto_list(request):
    productos = Producto.objects.all()
    return render(request, 'productos/listado.html', {'productos': productos})

# Vista para registrar (ya la debes tener)
def producto_new(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('producto_list')
    else:
        form = ProductoForm()
    return render(request, 'productos/registro.html', {'form': form, 'titulo': 'Registrar Producto'})

# NUEVA: Vista para detallar
def producto_detail(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, 'productos/detalle.html', {'producto': producto})

# NUEVA: Vista para editar
def producto_edit(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == "POST":
        # Se pasa la instancia existente para que Django sepa que debe actualizar, no crear
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('producto_list')
    else:
        form = ProductoForm(instance=producto)
    # Reutilizamos registro.html, pero le cambiamos el título
    return render(request, 'productos/registro.html', {'form': form, 'titulo': 'Editar Producto'})

# NUEVA: Vista para eliminar
def producto_delete(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == "POST":
        producto.delete()
        return redirect('producto_list')
    return render(request, 'productos/eliminar.html', {'producto': producto})