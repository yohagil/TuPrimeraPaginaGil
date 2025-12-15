from django.db import models

# Modelo 1: Autor (Requisito 1 de 3)
class Autor(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    profesion = models.CharField(max_length=40, default="Escritor")

    # Muestra el nombre completo en el administrador de Django
    def __str__(self):
        return f"{self.nombre} {self.apellido}"

# Modelo 2: Categoria (Requisito 2 de 3)
class Categoria(models.Model):
    nombre = models.CharField(max_length=40)

    def __str__(self):
        return self.nombre

# Modelo 3: Post (Requisito 3 de 3)
class Post(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    fecha_publicacion = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.titulo