from django import forms
from .models import Mensaje
from django.contrib.auth.models import User

class MensajeForm(forms.ModelForm):
    # Campo para elegir a quién se le envía el mensaje
    destinatario = forms.ModelChoiceField(
        queryset=User.objects.all(), 
        label="Para"
    )
    
    class Meta:
        model = Mensaje
        fields = ['destinatario', 'contenido']
        widgets = {
            'contenido': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Escribe tu mensaje aquí...'}),
        }