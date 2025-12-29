from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Esta línea es la "llave" que abre tu blog al entrar a http://127.0.0.1:8000/
    path('', include('blog.urls')), 
]