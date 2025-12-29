from django.shortcuts import render, redirect
from .models import Autor, Categoria, Post
from .forms import AutorFormulario, CategoriaFormulario, PostFormulario, BusquedaFormulario

def index(request):
    # Mostramos los últimos 10 posts
    posts = Post.objects.all().order_by('-id')[:10]
    return render(request, 'blog/index.html', {'posts': posts})

def crear_autor(request):
    if request.method == 'POST':
        formulario = AutorFormulario(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('index')
    else:
        formulario = AutorFormulario()
    return render(request, 'blog/crear_autor.html', {'formulario': formulario})

def crear_categoria(request):
    if request.method == 'POST':
        formulario = CategoriaFormulario(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('index')
    else:
        formulario = CategoriaFormulario()
    return render(request, 'blog/crear_categoria.html', {'formulario': formulario})

def crear_post(request):
    if request.method == 'POST':
        # IMPORTANTE: request.FILES es necesario para guardar la imagen
        formulario = PostFormulario(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('index')
    else:
        formulario = PostFormulario()
    return render(request, 'blog/crear_post.html', {'formulario': formulario})

def buscar_post(request):
    if request.method == 'POST':
        formulario = BusquedaFormulario(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            posts = Post.objects.filter(titulo__icontains=info['nombre'])
            return render(request, 'blog/index.html', {'posts': posts, 'busqueda': True})
    else:
        formulario = BusquedaFormulario()
    return render(request, 'blog/buscar_post.html', {'formulario': formulario})

def detalle_post(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, 'blog/detalle_post.html', {'post': post})
# --- NUEVA VISTA ACERCA DE MÍ ---
def about(request):
    return render(request, 'blog/about.html')

# --- IMPORTACIONES NUEVAS PARA CLASES ---
from django.views.generic import UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin # Requisito del Mixin
from django.urls import reverse_lazy

# --- CLASE PARA EDITAR POST ---
# LoginRequiredMixin: Exige estar logueado para editar (Seguridad)
class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostFormulario # Reutilizamos el formulario que ya hiciste
    template_name = 'blog/editar_post.html'
    success_url = reverse_lazy('index') # Al terminar, vuelve al inicio

# --- CLASE PARA BORRAR POST ---
class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'blog/borrar_post.html'
    success_url = reverse_lazy('index')
