#pip install djangorestframework
#pip install markdown       # Markdown support for the browsable API.
#pip install django-filter  # Filtering support

from rest_framework.exceptions import ValidationError, PermissionDenied
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import filters, status
from django_filters.rest_framework import DjangoFilterBackend
from .models import Calificacion, Mercado, Origen
from .serializers import CalificacionSerializer, MercadoSerializer, OrigenSerializer, CalcularFactoresSerializer
from .pagination import CustomPageNumberPagination

# Create your views here.
class CalculoFactoresAPIView(APIView):
    def post(self, req):
        serializer = CalcularFactoresSerializer(data=req.data)

        if serializer.is_valid():
            resultado = serializer.calcular_factores()
            return Response(resultado['factores'], status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CalificacionViewSet(ModelViewSet):
    queryset = Calificacion.objects.all().order_by('id')
    serializer_class = CalificacionSerializer

    pagination_class = CustomPageNumberPagination

    #Permitir que si el contenido de la data es una lista, entonces habilita el ingreso de varias calificaciones
    def get_serializer(self, *args, **kwargs):
        if kwargs.get('data') and isinstance(kwargs.get('data'), list):
            kwargs['many'] = True
        return super().get_serializer(*args, **kwargs)

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


