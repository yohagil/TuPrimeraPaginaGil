from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Ruta para el Blog (Página de inicio)
    path('', include('blog.urls')),
    
    # Ruta para Cuentas (Login, Registro, etc.)
    # Cuando alguien escriba "tupagina.com/accounts/...", Django buscará en la app accounts
    path('accounts/', include('accounts.urls')), 
    path('mensajeria/', include('mensajeria.urls')),
]

# Configuración para que las imágenes se vean mientras desarrollas (modo DEBUG)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)