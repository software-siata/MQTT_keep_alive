from django.db import models
from django.utils import timezone
import datetime


class Estaciones(models.Model):
    codigo = models.IntegerField()
    nombre = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=200)
    barrio_vereda = models.CharField(max_length=200)
    subcuenca = models.CharField(max_length=200)
    latitud = models.DecimalField(max_digits=9, decimal_places=6)
    longitud = models.DecimalField(max_digits=9, decimal_places=6)
    operador = models.CharField(max_length=200)
    ip = models.CharField(max_length=200)
    red = models.CharField(max_length=200) 
    estado = models.BooleanField()
    datos_enviados = models.IntegerField()
    topicos_enviados = models.IntegerField()
    datos_recuperados = models.IntegerField()
    ultima_actualizacion = models.DateTimeField()

    @property
    def estado_ultima_actualizacion(self):
        return self.ultima_actualizacion < timezone.now() - datetime.timedelta(minutes = 10)
    
    @property
    def porcentaje_enviados(self):
        return (self.datos_enviados / (self.topicos_enviados * 10)) * 100