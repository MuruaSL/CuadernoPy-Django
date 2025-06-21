from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.
def index(request):
    return render(request,"core/index.html")
    
def contenido(request):
    return render(request,"core/contenido.html")

def sobremi(request):
    return render(request, "core/sobremi.html")

# end def
