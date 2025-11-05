#pip install djangorestframework
#pip install markdown       # Markdown support for the browsable API.
#pip install django-filter  # Filtering support

from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from .models import Calificacion, Mercado, Origen
from .serializers import CalificacionSerializer, MercadoSerializer, OrigenSerializer

# Create your views here.
class CalificacionViewSet(ModelViewSet):
    queryset = Calificacion.objects.all()
    serializer_class = CalificacionSerializer

# pueden quedar solo lectura GET, por el momento GET, POST 
class MercadoViewSet(ModelViewSet): 
    queryset = Mercado.objects.all()
    serializer_class = MercadoSerializer

class OrigenViewSet(ModelViewSet):
    queryset = Origen.objects.all()
    serializer_class = OrigenSerializer



