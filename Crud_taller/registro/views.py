
# Create your views here.
from django.shortcuts import render, redirect
from .forms import AsistenciaForm

def registrar_asistencia(request):
    if request.method == 'POST':
        form = AsistenciaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registro_exitoso')
    else:
        form = AsistenciaForm()
    
    return render(request, 'registro/formulario.html', {'form': form})

def registro_exitoso(request):
    return render(request, 'registro/exito.html')