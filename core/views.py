from django.shortcuts import render, get_object_or_404, redirect
from .models import Curso, Clase
from .forms import ContactoFormulario, ClaseForm, CursoForm, CategoriaForm  # usado en sobremi
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

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

    #   Aplicacion de CBV - DetailView para detalles de clases 
class ClaseDetailView(DetailView):
    model = Clase
    template_name = 'core/clase_detalle.html'
    context_object_name = 'clase'
    
class ClaseCreateView(CreateView):
    model = Clase
    form_class = ClaseForm
    template_name = 'core/crear_clase.html'
    success_url = reverse_lazy('Cursos')


class ClaseUpdateView(UpdateView):
    model = Clase
    form_class = ClaseForm
    template_name = 'core/editar_clase.html'  
    success_url = reverse_lazy('Cursos')


class ClaseDeleteView(DeleteView):
    model = Clase
    template_name = 'core/eliminar_clase.html'
    success_url = reverse_lazy('Cursos')

def sobremi(request):
    if request.method == "POST":
        form = ContactoFormulario(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "core/sobremi.html", {"form": ContactoFormulario(), "exito": True})
    else:
        form = ContactoFormulario()
    return render(request, "core/sobremi.html", {"form": form})


#   Aplicacion de CBV - DetailView para detalles de clases 
class ClaseCreateView(CreateView):
    model = Clase
    form_class = ClaseForm
    template_name = 'core/crear_clase.html'
    success_url = reverse_lazy('Cursos')

# def crear_curso(request):
#     if request.method == "POST":
#         form = CursoForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('Cursos')
#     else:
#         form = CursoForm()
#     return render(request, 'core/crear_curso.html', {
#         'form': form,
#         'activo_administrativo': True 
#     })

class CursoCreateView(CreateView):
    model = Curso
    form_class = CursoForm
    template_name = 'core/crear_curso.html'
    success_url = reverse_lazy('Cursos')

class CursoUpdateView(UpdateView):
    model = Curso
    form_class = CursoForm
    template_name = 'core/editar_curso.html'
    success_url = reverse_lazy('Cursos')

class CursoDeleteView(DeleteView):
    model = Curso
    template_name = 'core/eliminar_curso.html'
    success_url = reverse_lazy('Cursos')
    
def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Cursos')
    else:
        form = CategoriaForm()
    return render(request, 'core/crear_categoria.html', {'form': form, 'activo_administrativo': True})