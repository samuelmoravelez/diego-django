from django.urls import path
from . import views

urlpatterns = [
    path('', views.registrar_asistencia, name='registrar_asistencia'),
    path('exito/', views.registro_exitoso, name='registro_exitoso'),
]
