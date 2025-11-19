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
    ejercicio = models.IntegerField(null=False)
    instrumento = models.CharField(max_length=3)
    fecha_pago = models.DateField(blank=True, null=True)
    origen = models.ForeignKey(Origen, on_delete=models.CASCADE, related_name='origenCalificacion')
    mercado = models.ForeignKey(Mercado, on_delete=models.CASCADE, related_name='mercadoCalificacion')
    periodo = models.IntegerField(default=0,null=False)
    secuencia_evento = models.IntegerField(default=0, null=False)
    factor_actualizacion = models.IntegerField(default=0, null=False)
    dividendo = models.IntegerField(default=0, null=False)
    valor_historico = models.FloatField(default=0.0, null=False)
    fechaActualizacion = models.DateField(blank=True, null=True)
    anio = models.DateField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.instrumento


 
