#pip install djangorestframework
#pip install markdown       # Markdown support for the browsable API.
#pip install django-filter  # Filtering support

from rest_framework import serializers
from .models import Calificacion, Mercado, Origen
import datetime


# Serializer para calcular factores a partir de montos
class CalcularFactoresSerializer(serializers.Serializer):
    montos = serializers.ListField(
        child=serializers.IntegerField(min_value=0), 
        allow_empty=False
    )

    def validate_montos(self, value):
        # factor 8 al 37 = 30 valores en total
        if len(value) < 30:
            raise serializers.ValidationError(
                "Debes enviar los montos desde la columna 8 hasta la 37."
            )
        return value

    def calcular_factores(self):
        montos = self.validated_data["montos"]
        base = sum(montos[0:12])

        if base == 0:
            factores = [0.0 for _ in montos]
        else:
            factores = [m / base for m in montos]

        # 8 decimales y 1 entero
        factores = [round(f, 8) for f in factores]

        return {
            "suma_base": base,
            "factores": factores
        }

class CalificacionSerializer(serializers.ModelSerializer):
    montos = serializers.ListField(write_only=True, required=False) #no se recibe con GET.

    def validate_instrumento(self, value):
        if len(value) != 3:
            raise serializers.ValidationError("El instrumento debe tener 3 caracteres")
        return value

    def validate_anio(self, value):
        anio_actual = datetime.date.today().year
        if value < 1950 or value > anio_actual:
            raise serializers.ValidationError("El año es inválido")
        return value

    def validate(self, data):
        fecha_pago = data.get("fecha_pago")
        fecha_actualizacion = data.get("fechaActualizacion")
        if fecha_pago and fecha_actualizacion:
            if fecha_actualizacion < fecha_pago:
                raise serializers.ValidationError({
                    "fechaActualizacion": "La fecha de actualización no puede ser menor a la fecha de pago"
                })
        return data

    def create(self, validated_data):
        montos = validated_data.pop("montos", None)
        if montos:
            calc_serializer = CalcularFactoresSerializer(data={"montos": montos})
            calc_serializer.is_valid(raise_exception=True)
            resultado = calc_serializer.calcular_factores() # funcion de CalcularFactorSerializer
            validated_data["factores"] = resultado["factores"]
        return super().create(validated_data)

    def update(self, instance, validated_data):
        montos = validated_data.pop("montos", None)
        if montos:
            calc_serializer = CalcularFactoresSerializer(data={"montos": montos})
            calc_serializer.is_valid(raise_exception=True)
            resultado = calc_serializer.calcular_factores() # funcion de CalcularFactorSerializer
            validated_data["factores"] = resultado["factores"]
        return super().update(instance, validated_data)

    class Meta:
        model = Calificacion
        fields = '__all__'
        
        


class MercadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mercado
        fields = '__all__'

class OrigenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Origen
        fields = '__all__'

        


