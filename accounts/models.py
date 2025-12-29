from django.db import models
from django.contrib.auth.models import User

class Avatar(models.Model):
    # Conectamos el Avatar con el Usuario (1 a 1)
    # on_delete=models.CASCADE significa que si borras al usuario, se borra su avatar
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    # Aquí se guardará la imagen. 'upload_to' crea una carpeta 'avatares' dentro de 'media'
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)

    def __str__(self):
        return f"Avatar de {self.user.username}"