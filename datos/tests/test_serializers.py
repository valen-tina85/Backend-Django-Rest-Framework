from django.test import TestCase
from datos.models import Calificacion, Origen, Mercado
from datos.serializers import CalificacionSerializer
from datetime import date

class CalificacionSerializerTest(TestCase):

    def setUp(self):
        self.origen = Origen.objects.create(nombre="Interno")
        self.mercado = Mercado.objects.create(nombre="Local")

    def test_serializer_valido(self):
        data = {
            "ejercicio": 2024,
            "instrumento": "ABC",
            "fecha_pago": date(2024, 1, 10),
            "origen": self.origen.id,
            "mercado": self.mercado.id,
            "periodo": 1,
            "secuencia_evento": 1,
            "factor_actualizacion": 0,
            "dividendo": 0,
            "valor_historico": 10.0,
            "fechaActualizacion": date(2024, 2, 1),
            "anio": 2024,
            "factores": [0.1, 0.2],
        }
        serializer = CalificacionSerializer(data=data)
        self.assertTrue(serializer.is_valid(), serializer.errors)

    def test_serializer_invalido_factores(self):
        data = {
            "ejercicio": 2024,
            "instrumento": "ABC",
            "fecha_pago": date(2024, 1, 10),
            "origen": self.origen.id,
            "mercado": self.mercado.id,
            "periodo": 1,
            "secuencia_evento": 1,
            "factor_actualizacion": 0,
            "dividendo": 0,
            "valor_historico": 10.0,
            "fechaActualizacion": date(2024, 2, 1),
            "anio": 2024,
            "factores": "no es lista",
        }
        serializer = CalificacionSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("factores", serializer.errors)