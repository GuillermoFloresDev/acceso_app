# main/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('validar/', views.validar_usuario, name='validar_usuario'),
    path('foto/', views.tomar_foto, name='tomar_foto'),
    path('logout/', views.cerrar_sesion, name='cerrar_sesion'),
]
