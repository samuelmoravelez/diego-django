#!/usr/bin/env python
"""
Utilidad de línea de comandos de Django para tareas administrativas.

Punto de entrada para ejecutar el servidor de desarrollo, migraciones,
createsuperuser y otros comandos de gestión del proyecto tienda.
"""
import os
import sys


def main():
    """
    Configura Django y ejecuta el comando indicado en la terminal.

    Establece DJANGO_SETTINGS_MODULE antes de importar el núcleo de gestión.
    Los argumentos se leen desde sys.argv (p. ej. runserver, migrate).

    Raises:
        ImportError: Si Django no está instalado o el entorno virtual no está activo.

    Returns:
        None
    """
    # Carga la configuración del proyecto (apps, BD, URLs del CRUD)
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tienda.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    # Delega runserver, makemigrations, migrate, etc. según sys.argv
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
