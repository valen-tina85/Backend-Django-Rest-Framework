from django.test import TestCase
from django.core.exceptions import ValidationError
from datetime import date

from datos.models import Calificacion, Origen, Mercado

class CalificacionModelTests(TestCase):

    def setUp(self):
        self.origen = Origen.objects.create(nombre="Chile")
        self.mercado = Mercado.objects.create(nombre="SII")

    def test_instrumento_debe_tener_tres_caracteres(self):
        cal = Calificacion(
            ejercicio=2024,
            instrumento="AB",  # Solo 2 caracteres → error
            fecha_pago=date(2024, 1, 10),
            origen=self.origen,
            mercado=self.mercado,
            periodo=1,
            secuencia_evento=1,
            factor_actualizacion=1,
            dividendo=1,
            valor_historico=10.5,
            fechaActualizacion=date(2024, 1, 20),
            anio=2024,
            factores=[]
        )

        with self.assertRaises(ValidationError):
            cal.clean()

    def test_fecha_actualizacion_no_debe_ser_menor_a_fecha_pago(self):
        cal = Calificacion(
            ejercicio=2024,
            instrumento="ABC",
            fecha_pago=date(2024, 1, 20),
            origen=self.origen,
            mercado=self.mercado,
            periodo=1,
            secuencia_evento=1,
            factor_actualizacion=1,
            dividendo=1,
            valor_historico=10.5,
            fechaActualizacion=date(2024, 1, 10),  # menor → error
            anio=2024,
            factores=[]
        )

        with self.assertRaises(ValidationError):
            cal.clean()

    def test_factores_debe_ser_lista(self):
        cal = Calificacion(
            ejercicio=2024,
            instrumento="ABC",
            fecha_pago=date(2024, 1, 10),
            origen=self.origen,
            mercado=self.mercado,
            periodo=1,
            secuencia_evento=1,
            factor_actualizacion=1,
            dividendo=1,
            valor_historico=10.5,
            fechaActualizacion=date(2024, 1, 20),
            anio=2024,
            factores="esto NO es una lista"  # error
        )

        with self.assertRaises(ValidationError):
            cal.clean()