from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.
def index(request):
    return render(request,"core/index.html")
    
# end def

def saludar(request):
    return HttpResponse("Hola desde Django")

def saludar_con_etiqueta(request):
    return HttpResponse('<h1 style= "color:red">Hola mundo</h1>')
    
def saludar_con_parametros(request,nombre:str,apellido:str):
    return HttpResponse('<h1 style= "color:red">Hola </h1>  {{ nombre }} {{ apellido }}')
    
