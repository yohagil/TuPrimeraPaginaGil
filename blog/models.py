from django.db import models
from ckeditor.fields import RichTextField # Importamos el editor de texto rico

# Modelo 1: Autor
class Autor(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    profesion = models.CharField(max_length=40, default="Escritor")

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

# Modelo 2: Categoria
class Categoria(models.Model):
    nombre = models.CharField(max_length=40)

    def __str__(self):
        return self.nombre

# Modelo 3: Post (MEJORADO)
class Post(models.Model):
    titulo = models.CharField(max_length=100)
    
    # Usamos RichTextField en lugar de TextField para tener formato (negritas, etc.)
    contenido = RichTextField()
    
    # Campo para subir la imagen de portada del post
    # null=True, blank=True permite crear posts sin imagen obligatoria
    imagen = models.ImageField(upload_to='posts', null=True, blank=True)
    
    fecha_publicacion = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.titulo