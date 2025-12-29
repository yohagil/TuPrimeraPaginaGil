from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm
from .models import Avatar # Importamos el modelo Avatar que acabamos de crear

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contra)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                return render(request, "accounts/login.html", {"mensaje": "Error: Datos incorrectos", "form": form})
        else:
            return render(request, "accounts/login.html", {"mensaje": "Error: Formulario inválido", "form": form})
    
    form = AuthenticationForm()
    return render(request, "accounts/login.html", {"form": form})

def register_request(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, "accounts/register.html", {"form": form})

@login_required
def ver_perfil(request):
    # Buscamos si el usuario tiene un avatar guardado
    try:
        avatar = Avatar.objects.get(user=request.user)
        imagen_url = avatar.imagen.url
    except Avatar.DoesNotExist:
        imagen_url = None # Si no tiene, enviamos None para mostrar una imagen por defecto

    return render(request, "accounts/profile.html", {"url": imagen_url})

@login_required
def editar_perfil(request):
    usuario = request.user
    
    if request.method == 'POST':
        # Es vital agregar request.FILES para recibir archivos (imágenes)
        form = UserUpdateForm(request.POST, request.FILES, instance=usuario)
        
        if form.is_valid():
            form.save() # Guarda los datos básicos (email, nombre)
            
            # Lógica extra para guardar la imagen en el modelo Avatar
            img_file = form.cleaned_data.get('imagen')
            if img_file:
                # Verificamos si ya existe un avatar para actualizarlo o crear uno nuevo
                try:
                    avatar = Avatar.objects.get(user=usuario)
                    avatar.imagen = img_file
                    avatar.save()
                except Avatar.DoesNotExist:
                    avatar = Avatar(user=usuario, imagen=img_file)
                    avatar.save()
            
            return redirect('profile')
    else:
        form = UserUpdateForm(instance=usuario)
        
    return render(request, "accounts/editar_perfil.html", {"form": form})