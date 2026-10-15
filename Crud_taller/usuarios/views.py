from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User



def iniciar_sesion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirige a la página de inicio después del inicio de sesión
        else:
            error_message = 'Nombre de usuario o contraseña incorrectos.'
            return render(request, 'usuarios/login.html', {'error_message': error_message})
    else:
        return render(request, 'usuarios/login.html')



def cerrar_sesion(request):
    logout(request)
    return redirect("/usuarios/login/")         # Redirige a la página de inicio de sesión después de cerrar sesión