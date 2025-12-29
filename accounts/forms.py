from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    # Agregamos el campo de imagen (Avatar)
    # required=False permite que el usuario guarde cambios sin obligación de subir foto
    imagen = forms.ImageField(required=False, label="Imagen de Perfil")
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']