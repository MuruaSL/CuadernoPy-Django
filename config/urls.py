"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from core import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="Index"),
    path("sobremi/", views.sobremi, name="SobreMi"),
    path('admin/', admin.site.urls),
    
    # URLS de curso
    path("cursos/", views.cursos, name="Cursos"),
    path("curso/<int:curso_id>/", views.curso_detalle, name="CursoDetalle"),
    path('crear_curso/', views.CursoCreateView.as_view(), name='CrearCurso'),
    path('editar_curso/<int:pk>/', views.CursoUpdateView.as_view(), name='EditarCurso'),
    path('eliminar_curso/<int:pk>/', views.CursoDeleteView.as_view(), name='EliminarCurso'),
    
    # URLS de categoria
    path('crear_categoria/', views.crear_categoria, name='CrearCategoria'),
    
    # URLS de clase
    path('crear_clase/', views.ClaseCreateView.as_view(), name='CrearClase'),
    path('clase/<int:pk>/', views.ClaseDetailView.as_view(), name='clase_detalle'),
    path('editar_clase/<int:pk>/', views.ClaseUpdateView.as_view(), name='EditarClase'),
    path('eliminar_clase/<int:pk>/', views.ClaseDeleteView.as_view(), name='EliminarClase'),
    
    # URLS de perfil (Accounts)
    path('accounts/', include('accounts.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
