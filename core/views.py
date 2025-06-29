from django.shortcuts import render, get_object_or_404, redirect
from .models import MensajeContacto, Curso, Clase
from .forms import ContactoFormulario, ClaseForm, CursoForm, CategoriaForm  # usado en sobremi

def index(request):
    return render(request, "core/index.html")

def cursos(request):
    query = request.GET.get('q', '')
    if query:
        cursos = Curso.objects.filter(titulo__icontains=query)
    else:
        cursos = Curso.objects.all()
    return render(request, 'core/cursos.html', {'cursos': cursos, 'query': query})


def curso_detalle(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    query = request.GET.get('q', '')
    
    if query:
        clases = curso.clases.filter(titulo__icontains=query)
    else:
        clases = curso.clases.all()
    
    return render(request, "core/curso_detalle.html", {
        "curso": curso,
        "clases": clases,
        "query": query
    })

def clase_detalle(request, clase_id):
    clase = get_object_or_404(Clase, id=clase_id)
    return render(request, "core/clase_detalle.html", {"clase": clase})

def sobremi(request):
    if request.method == "POST":
        form = ContactoFormulario(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "core/sobremi.html", {"form": ContactoFormulario(), "exito": True})
    else:
        form = ContactoFormulario()
    return render(request, "core/sobremi.html", {"form": form})


def crear_clase(request):
    if request.method == "POST":
        form = ClaseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("Cursos")
    else:
        form = ClaseForm()
    return render(request, "core/crear_clase.html", {"form": form})

def crear_curso(request):
    if request.method == "POST":
        form = CursoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Cursos')
    else:
        form = CursoForm()
    return render(request, 'core/crear_curso.html', {
        'form': form,
        'activo_administrativo': True 
    })

def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Cursos')
    else:
        form = CategoriaForm()
    return render(request, 'core/crear_categoria.html', {'form': form, 'activo_administrativo': True})