from django.http import HttpResponse #libreria para dar respuestas

def home(request):
    return HttpResponse("Hello, World!")