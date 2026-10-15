from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.db.models import Q
from .models import Producto, Pedido
from .forms import ProductoForm, PedidoForm

# --- Autenticación ---
def login_view(request):
    if request.user.is_authenticated:
        return redirect('producto_list')

    form = AuthenticationForm(request, data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"¡Bienvenido, {user.username}!")
            return redirect('producto_list')
        else:
            messages.error(request, "Usuario o contraseña incorrectos.")

    return render(request, 'core/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    messages.info(request, "Has cerrado sesión correctamente.")
    return redirect('login')


# --- CRUD Productos ---
@login_required
def producto_list(request):
    query = request.GET.get('q', '')
    productos = Producto.objects.all()
    if query:
        productos = productos.filter(Q(nombre__icontains=query) | Q(descripcion__icontains=query))
    return render(request, 'core/producto_list.html', {'productos': productos, 'query': query})

@login_required
def producto_create(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Producto creado exitosamente.")
            return redirect('producto_list')
    else:
        form = ProductoForm()
    return render(request, 'core/producto_form.html', {'form': form, 'title': 'Crear Producto'})

@login_required
def producto_update(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, "Producto actualizado exitosamente.")
            return redirect('producto_list')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'core/producto_form.html', {'form': form, 'title': 'Editar Producto', 'producto': producto})

@login_required
def producto_delete(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        messages.success(request, "Producto eliminado correctamente.")
        return redirect('producto_list')
    return render(request, 'core/producto_confirm_delete.html', {'producto': producto})


# --- CRUD Pedidos ---
@login_required
def pedido_list(request):
    query = request.GET.get('q', '')
    pedidos = Pedido.objects.select_related('usuario').all()
    if query:
        pedidos = pedidos.filter(Q(cliente__icontains=query) | Q(numero_pedido__icontains=query))
    return render(request, 'core/pedido_list.html', {'pedidos': pedidos, 'query': query})

@login_required
def pedido_create(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            pedido = form.save(commit=False)
            pedido.usuario = request.user
            pedido.save()
            messages.success(request, "Pedido registrado exitosamente.")
            return redirect('pedido_list')
    else:
        form = PedidoForm()
    return render(request, 'core/pedido_form.html', {'form': form, 'title': 'Registrar Pedido'})

@login_required
def pedido_update(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    if request.method == 'POST':
        form = PedidoForm(request.POST, instance=pedido)
        if form.is_valid():
            form.save()
            messages.success(request, "Pedido actualizado exitosamente.")
            return redirect('pedido_list')
    else:
        form = PedidoForm(instance=pedido)
    return render(request, 'core/pedido_form.html', {'form': form, 'title': 'Editar Pedido', 'pedido': pedido})

@login_required
def pedido_delete(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    if request.method == 'POST':
        pedido.delete()
        messages.success(request, "Pedido eliminado correctamente.")
        return redirect('pedido_list')
    return render(request, 'core/pedido_confirm_delete.html', {'pedido': pedido})