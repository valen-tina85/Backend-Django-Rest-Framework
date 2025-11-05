from django.db import models

# Create your models here.

class Origen(models.Model):
    nombre = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

class Mercado(models.Model):
    nombre = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

class Calificacion(models.Model):
    ejercicio = models.IntegerField()
    instrumento = models.CharField(max_length=3)
    fecha_pago = models.DateField()
    origen = models.ForeignKey(Origen, on_delete=models.CASCADE, related_name='origenCalificacion')
    mercado = models.ForeignKey(Mercado, on_delete=models.CASCADE, related_name='mercadoCalificacion')

 
