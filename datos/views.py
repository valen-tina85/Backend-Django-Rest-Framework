#pip install djangorestframework
#pip install markdown       # Markdown support for the browsable API.
#pip install django-filter  # Filtering support

from rest_framework.exceptions import ValidationError, PermissionDenied
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
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

    def perform_destroy(self, instance):
        if instance.mercado_calificacion.exists():
            raise ValidationError("No puedes eliminar un mercado que tiene calificaciones asociadas")
        instance.delete()

class OrigenViewSet(ModelViewSet):
    queryset = Origen.objects.all()
    serializer_class = OrigenSerializer

    def perform_destroy(self, instance):
        if instance.origen_calificacion.exists():
            raise ValidationError("No puedes eliminar un origen que está asociado a calificaciones")
        instance.delete()


