from django.shortcuts import render
from .models import Estaciones

# Create your views here.

def list(request):
    estaciones = Estaciones.objects.all()
    return render(request, "estado_estaciones/list_estaciones.html", {'estaciones': estaciones})