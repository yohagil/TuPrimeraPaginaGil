from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import login_request, register_request, editar_perfil, ver_perfil

urlpatterns = [
    path('login/', login_request, name='login'),
    path('register/', register_request, name='register'),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('profile/', ver_perfil, name='profile'),
    path('profile/edit/', editar_perfil, name='editar_perfil'),
]