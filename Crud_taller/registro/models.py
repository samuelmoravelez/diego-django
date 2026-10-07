from django.db import models

class Asistencia(models.Model):
    # No es necesario crear el campo 'id', Django lo crea y administra automáticamente
    
    TIPO_DOC_CHOICES = [
        ('CC', 'Cédula de Ciudadanía'),
        ('TI', 'Tarjeta de Identidad'),
        ('CE', 'Cédula de Extranjería'),
        ('PAS', 'Pasaporte'),
    ]

    tipo_documento = models.CharField(max_length=3, choices=TIPO_DOC_CHOICES)
    documento = models.CharField(max_length=20)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    whatsapp = models.CharField(max_length=20)
    fecha = models.DateField()
    asistio = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nombres} {self.apellidos} - {self.fecha}"