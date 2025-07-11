from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import FormularioPerfil, RegistroUsuarioForm, LoginUsuarioForm,FormularioUsuario
from django.contrib.auth.views import LoginView
from django.contrib import messages

@login_required
def ver_perfil(request):
    return render(request, 'accounts/perfil.html', {'perfil': request.user.profile})

@login_required
def editar_perfil(request):
    if request.method == 'POST':
        form_usuario = FormularioUsuario(request.POST, instance=request.user)
        form_perfil = FormularioPerfil(request.POST, request.FILES, instance=request.user.profile)
        if form_usuario.is_valid() and form_perfil.is_valid():
            form_usuario.save()
            form_perfil.save()
            return redirect('ver_perfil')
    else:
        form_usuario = FormularioUsuario(instance=request.user)
        form_perfil = FormularioPerfil(instance=request.user.profile)
    return render(request, 'accounts/editar_perfil.html', {
        'form_usuario': form_usuario,
        'form_perfil': form_perfil,
    })

def registro(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "¡Registro exitoso! Ya podés iniciar sesión.")
            return redirect('login')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'accounts/registro.html', {'form': form})

class LoginPersonalizadoView(LoginView):
    authentication_form = LoginUsuarioForm
