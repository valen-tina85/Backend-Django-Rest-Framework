#pip install djangorestframework
#pip install markdown       # Markdown support for the browsable API.
#pip install django-filter  # Filtering support

from rest_framework import serializers
from .models import Calificacion, Mercado, Origen
import datetime

class CalificacionSerializer(serializers.ModelSerializer):

    def validate_instrumento(self, value):
        if len(value) !=3:
            raise serializers.ValidationError("El instrumento debe tener 3 caracteres")
        return value
    
    def validate_factores(self,value):
        if not isinstance(value, list):
            raise serializers.ValidationError("Los factores no cumplen con el formato esperado") 
        for val in value:
            if not isinstance(val, (int,float)):
                raise serializers.ValidationError("Todos los factores deben ser números")
            if val > 1:
                raise serializers.ValidationError("Los valores del factor no deben ser mayor a 1")
            if val < 0:
                raise serializers.ValidationError("No se aceptan valores del factor negativos")
        return value
    
    def validate_anio(self, value):
        anio_actual = datetime.date.today().year #rango valido de años
        if value < 1950 or value > anio_actual:
            raise serializers.ValidationError("El año es inválido")
        return value
    
    def validate(self, data):
        fecha_pago = data.get("fecha_pago")
        fecha_actualizacion = data.get("fechaActualizacion")

        if fecha_actualizacion and fecha_pago: #ambos deben existir
            if fecha_actualizacion < fecha_pago:
                raise serializers.ValidationError({"fechaActualizacion": "La fecha de actualización no puede ser menor a la fecha de pago"})
        return data

    class Meta:
        model = Calificacion #de donde se sacan los datos
        fields = '__all__' #orden de sacar todos los datos del modelo Calificacion
        
        def validate_factores(self,value):
            for val in value:
                if val > 1:
                    raise serializers.ValidationError("Los valores del factor no puede ser mayor a 1")
            return value



class MercadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mercado
        fields = '__all__'

class OrigenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Origen
        fields = '__all__'

        


