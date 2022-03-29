from django.urls import path
from . import views

urlpatterns = [
    path('estaciones/listar', views.list, name='estaciones_listar'),
]