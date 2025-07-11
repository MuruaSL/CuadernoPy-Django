from django.urls import path
from . import views

from .forms import LoginUsuarioForm
from .views import registro
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('perfil/', views.ver_perfil, name='ver_perfil'),
    path('perfil/editar/', views.editar_perfil, name='editar_perfil'),
    #Gestion de sesiones
    path('registro/', registro, name='registro'),
    path('login/',auth_views.LoginView.as_view(template_name='accounts/login.html',authentication_form=LoginUsuarioForm),
    name='login'
),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('password_change/', auth_views.PasswordChangeView.as_view(
        template_name='accounts/cambiar_contrasena.html',
        success_url='/accounts/password_change/done/'
    ), name='password_change'),
    
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='accounts/cambiar_contrasena_realizada.html'
    ), name='password_change_done'),
]
