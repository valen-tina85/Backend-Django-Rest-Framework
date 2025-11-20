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
    instrumento = models.CharField(max_length=3, blank=False, null=False)
    fecha_pago = models.DateField(null=False)
    origen = models.ForeignKey(Origen, on_delete=models.PROTECT, related_name='origen_calificacion')
    mercado = models.ForeignKey(Mercado, on_delete=models.PROTECT, related_name='mercado_calificacion')
    periodo = models.IntegerField(default=0,null=False)
    secuencia_evento = models.IntegerField(default=0, null=False)
    factor_actualizacion = models.IntegerField(default=0, null=False)
    dividendo = models.IntegerField(default=0, null=False)
    valor_historico = models.FloatField(default=0.0, null=False)
    fechaActualizacion = models.DateField(null=False)
    anio = models.DateField("Año", null=False)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ["-instrumento","periodo"]

    def __str__(self) -> str:
        return f"Calificación {self.instrumento} - {self.ejercicio}"


 
