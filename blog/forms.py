from django import forms
from .models import Autor, Categoria, Post

# Formulario Automático para Autor
class AutorFormulario(forms.ModelForm):
    class Meta:
        model = Autor
        fields = '__all__' # Crea inputs para todos los campos del modelo

# Formulario Automático para Categoría
class CategoriaFormulario(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'

# Formulario Automático para Post
class PostFormulario(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

# Formulario Manual para Búsqueda (Este no guarda datos, solo busca)
class BusquedaFormulario(forms.Form):
    nombre = forms.CharField()