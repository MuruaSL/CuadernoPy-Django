from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .forms import ContactoFormulario
from .models import MensajeContacto
# Create your views here.
def index(request):
    return render(request,"core/index.html")
    
def contenido(request):
    return render(request,"core/contenido.html")

def sobremi(request):
    return render(request, "core/sobremi.html")

def sobremi(request):
    if request.method == "POST":
        form = ContactoFormulario(request.POST)
        if form.is_valid():
            # Extraer los datos
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            mensaje = form.cleaned_data['mensaje']

            # Guardar en la base de datos
            MensajeContacto.objects.create(
                nombre=nombre,
                email=email,
                mensaje=mensaje
            )

            return render(request, "core/sobremi.html", {"form": ContactoFormulario(), "exito": True})
    else:
        form = ContactoFormulario()

    return render(request, "core/sobremi.html", {"form": form})

# end def
