from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from .forms import ContactoFormulario, ContenidoForm
from .models import MensajeContacto
from .models import Contenido 

from django.shortcuts import get_object_or_404
# Create your views here.
def index(request):
    return render(request,"core/index.html")
    
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


def ver_contenido(request):
    contenidos = Contenido.objects.all()
    return render(request, "core/contenido.html", {"contenidos": contenidos})

def detalle_contenido(request, contenido_id):
    contenido = get_object_or_404(Contenido, id=contenido_id)
    return render(request, "core/contenido_detalle.html", {"contenido": contenido})

def crear_contenido(request):
    if request.method == "POST":
        form = ContenidoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("Contenido")  # ← este debe ser el name del path en urls.py
    else:
        form = ContenidoForm()
    return render(request, "core/crear_contenido.html", {"form": form})