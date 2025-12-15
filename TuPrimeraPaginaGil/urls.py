from django.contrib import admin
from django.urls import path
from blog.views import index, crear_autor, crear_categoria, crear_post, buscar_post

urlpatterns = [
    # Ruta de administración de Django (siempre incluida)
    path('admin/', admin.site.urls),

    # Rutas del Blog:
    path('', index, name='index'), # La página principal (la raíz del sitio)
    path('crear_autor/', crear_autor, name='crear_autor'),
    path('crear_categoria/', crear_categoria, name='crear_categoria'),
    path('crear_post/', crear_post, name='crear_post'),
    path('buscar_post/', buscar_post, name='buscar_post'),
]