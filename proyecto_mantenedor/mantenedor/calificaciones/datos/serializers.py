#pip install djangorestframework
#pip install markdown       # Markdown support for the browsable API.
#pip install django-filter  # Filtering support

from rest_framework import serializers
from .models import Calificacion, Mercado, Origen

class CalificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calificacion #de donde se sacan los datos
        fields = '__all__' #orden de sacar todos los datos del modelo Calificacion

class MercadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mercado
        fields = '__all__'

class OrigenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Origen
        fields = '__all__'

        


