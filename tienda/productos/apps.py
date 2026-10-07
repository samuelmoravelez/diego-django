"""Configuración de la aplicación Django productos."""

from django.apps import AppConfig


class ProductosConfig(AppConfig):
    """
    Metadatos de la app productos para el registro en INSTALLED_APPS.

    Attributes:
        name (str): Ruta Python del paquete de la aplicación ('productos').
    """

    name = 'productos'
