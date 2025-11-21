from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from datos.models import Calificacion, Origen, Mercado
from datetime import date

class CalificacionViewTests(APITestCase):
    def setUp(self):
        self.origen = Origen.objects.create(nombre="Interno")
        self.mercado = Mercado.objects.create(nombre="Local")
        self.calificacion_data = {
            "ejercicio": 2024,
            "instrumento": "ABC",
            "fecha_pago": "2024-01-10",
            "origen": self.origen.id,
            "mercado": self.mercado.id,
            "periodo": 1,
            "secuencia_evento": 1,
            "factor_actualizacion": 0,
            "dividendo": 0,
            "valor_historico": 10.0,
            "fechaActualizacion": "2024-02-01",
            "anio": 2024,
            "factores": [0.1, 0.2]
        }

    def test_list_calificaciones(self):
        url = reverse('calificacion-list')  # name definido por el router
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_calificacion(self):
        url = reverse('calificacion-list')
        response = self.client.post(url, self.calificacion_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Calificacion.objects.count(), 1)
        self.assertEqual(Calificacion.objects.get().instrumento, "ABC")


class MercadoViewTests(APITestCase):
    def setUp(self):
        self.mercado = Mercado.objects.create(nombre="Local")

    def test_list_mercados(self):
        url = reverse('mercado-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_mercado_con_calificacion(self):
        origen = Origen.objects.create(nombre="Interno")
        Calificacion.objects.create(
            ejercicio=2024,
            instrumento="XYZ",
            fecha_pago="2024-01-01",
            origen=origen,
            mercado=self.mercado,
            periodo=1,
            secuencia_evento=1,
            factor_actualizacion=0,
            dividendo=0,
            valor_historico=10,
            fechaActualizacion="2024-01-10",
            anio=2024,
            factores=[]
        )
        url = reverse('mercado-detail', args=[self.mercado.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class OrigenViewTests(APITestCase):
    def setUp(self):
        self.origen = Origen.objects.create(nombre="Interno")

    def test_list_origenes(self):
        url = reverse('origen-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_origen_con_calificacion(self):
        mercado = Mercado.objects.create(nombre="Local")
        Calificacion.objects.create(
            ejercicio=2024,
            instrumento="XYZ",
            fecha_pago="2024-01-01",
            origen=self.origen,
            mercado=mercado,
            periodo=1,
            secuencia_evento=1,
            factor_actualizacion=0,
            dividendo=0,
            valor_historico=10,
            fechaActualizacion="2024-01-10",
            anio=2024,
            factores=[]
        )
        url = reverse('origen-detail', args=[self.origen.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
