from django.shortcuts import render, redirect
from .models import Autor, Categoria, Post
from .forms import AutorFormulario, CategoriaFormulario, PostFormulario, BusquedaFormulario

# 1. Vista de Inicio (Index)
def index(request):
    # Traemos los últimos 10 posts para mostrarlos en el inicio
    posts = Post.objects.all().order_by('-id')[:10]
    return render(request, 'blog/index.html', {'posts': posts})

# 2. Vista para Crear Autor
def crear_autor(request):
    if request.method == 'POST':
        formulario = AutorFormulario(request.POST)
        if formulario.is_valid():
            formulario.save() # ¡Magia de ModelForm! Guarda directo en BD
            return redirect('index')
    else:
        formulario = AutorFormulario()
    return render(request, 'blog/crear_autor.html', {'formulario': formulario})

# 3. Vista para Crear Categoría
def crear_categoria(request):
    if request.method == 'POST':
        formulario = CategoriaFormulario(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('index')
    else:
        formulario = CategoriaFormulario()
    return render(request, 'blog/crear_categoria.html', {'formulario': formulario})

# 4. Vista para Crear Post
def crear_post(request):
    if request.method == 'POST':
        formulario = PostFormulario(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('index')
    else:
        formulario = PostFormulario()
    return render(request, 'blog/crear_post.html', {'formulario': formulario})

# 5. Vista para Buscar Post
def buscar_post(request):
    if request.method == 'POST':
        formulario = BusquedaFormulario(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            # Filtramos los posts por título
            posts = Post.objects.filter(titulo__icontains=info['nombre'])
            return render(request, 'blog/index.html', {'posts': posts, 'busqueda': True})
    else:
        formulario = BusquedaFormulario()
    return render(request, 'blog/buscar_post.html', {'formulario': formulario})