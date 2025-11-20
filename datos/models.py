from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
import datetime

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
    ejercicio = models.IntegerField(validators=[MinValueValidator(1950)],null=False)
    instrumento = models.CharField(max_length=3, blank=False, null=False)
    fecha_pago = models.DateField(null=False)
    origen = models.ForeignKey(Origen, on_delete=models.PROTECT, related_name='origen_calificacion')
    mercado = models.ForeignKey(Mercado, on_delete=models.PROTECT, related_name='mercado_calificacion')
    periodo = models.IntegerField(default=0,validators=MinValueValidator[0],null=False)
    secuencia_evento = models.IntegerField(default=0, validators=MinValueValidator[0], null=False)
    factor_actualizacion = models.IntegerField(default=0, null=False)
    dividendo = models.IntegerField(default=0, validators=MinValueValidator[0], null=False)
    valor_historico = models.FloatField(default=0.0, validators=MinValueValidator[0.0], null=False)
    fechaActualizacion = models.DateField(null=False)
    anio = models.IntegerField("Año", validators=[MinValueValidator(1950),MaxValueValidator(datetime.date.today().year)],null=False)
    descripcion = models.TextField(blank=True, null=True)
    factores = models.JSONField(default=list)

    class Meta:
        ordering = ["-instrumento","periodo"]

    def clean(self):
        errors = {}

        if len(self.instrumento) != 3:
            errors["instrumento"] = "El instrumento debe tener 3 caracteres"

        if self.fechaActualizacion < self.fecha_pago:
            errors["fechaActualizacion"] = "La fecha de actualización no debe ser menor a la fecha de pago"
        # validar que los factores vienen en lista
        if not isinstance(self.factores, list): #isinstance(valor,tipo) verifica si un valor es el indicado
            errors["factores"] = "Los factores tienen un error de formato"

        if errors:
            raise ValidationError(errors)

    def __str__(self) -> str:
        return f"Calificación {self.instrumento} - {self.ejercicio}"


 
