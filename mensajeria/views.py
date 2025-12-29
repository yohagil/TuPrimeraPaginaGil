from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Mensaje
from .forms import MensajeForm

@login_required
def inbox(request):
    # Filtramos los mensajes donde el destinatario es el usuario actual
    # order_by('-fecha_envio') muestra los más recientes primero
    mensajes = Mensaje.objects.filter(destinatario=request.user).order_by('-fecha_envio')
    return render(request, 'mensajeria/inbox.html', {'mensajes': mensajes})

@login_required
def enviar_mensaje(request):
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            mensaje = form.save(commit=False)
            mensaje.remitente = request.user # El que envía es el usuario logueado
            mensaje.save()
            return redirect('inbox')
    else:
        form = MensajeForm()
        # Truco: Quitamos al usuario actual de la lista de destinatarios (para no enviarse a sí mismo)
        form.fields['destinatario'].queryset = User.objects.exclude(username=request.user.username)
    
    return render(request, 'mensajeria/enviar_mensaje.html', {'form': form})