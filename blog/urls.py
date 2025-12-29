from django.urls import path
from . import views

# Estas son las rutas específicas de tu aplicación de Blog
urlpatterns = [
    # Ruta para la página de inicio (donde se ven los posts)
    path('', views.index, name='index'),
    
    # Rutas para los formularios de creación
    path('crear-autor/', views.crear_autor, name='crear_autor'),
    path('crear-categoria/', views.crear_categoria, name='crear_categoria'),
    path('crear-post/', views.crear_post, name='crear_post'),
    
    # Ruta para el formulario de búsqueda
    path('buscar-post/', views.buscar_post, name='buscar_post'),
    path('post/<int:pk>/', views.detalle_post, name='detalle_post'),
    path('about/', views.about, name='about'),
      path('post/editar/<int:pk>/', views.PostUpdateView.as_view(), name='editar_post'),
    path('post/borrar/<int:pk>/', views.PostDeleteView.as_view(), name='borrar_post'),

]