from main import TransaccionPago
from main import Pago
from datetime import datetime
import unittest

class Mis_test(unittest.TestCase):

    #NACHO
    def test_titularTarjetaString(self):
        self.assertTrue(TransaccionPago("Pedro Fernandez", 1234, "En espera").esNombreTitularString())

    #NACHO
    def test_titularTarjetaCadenaVacia(self):
        self.assertFalse(TransaccionPago("Pedro Fernandez", 1234, "En espera").esNombreCadenaVacia())

    #NACHO
    def test_fechaActualTransaccion(self):
        self.assertEqual(TransaccionPago("Pedro Fernandez", 1234, "En espera").fechaActualTransaccion, datetime.today())

    #JUN
    def test_CodigoPagoAlfanumerico(self):
        self.assertTrue(Pago("ASDF123456", 1234, 5000.22, "Pendiente").codigoContieneSoloAlfanumericos())

    def test_estadoPendientePago(self):
        self.assertTrue(Pago("ASDF123456", 1234, 5000.22, "Pendiente").esEstadoPendiente())

    # #SARA
    def test_titularAlfabetico(self):
        self.assertTrue(TransaccionPago("Victor Nomberto", 1234, "En espera").esNombreAlfabetico())

    def test_CodigoCuatroTarjetaTransaccion(self):
        self.assertTrue(TransaccionPago("Pedro Fernandez", 1234, "En espera").cuatroDigitosTarjetaTransaccion())

    # FRANCO
    def test_CodigoPagoTipoFloat(self):
        self.assertTrue(Pago("ASDF123456", 1234, 5000.22, "Pendiente").isfloat())

    def test_CodigoPagoTieneOchoDigitos(self):
        self.assertFalse(Pago("ASDF123456", 1234, 5000.22, "Pendiente").tieneOchoDigitosCodigoPago())

    #JULI MI VIDA <3
    def test_NumeroTarjetaTransaccionEntero(self):
        self.assertTrue(TransaccionPago("Pedro Fernandez", 1234, "En espera").numeroTransaccionInt())

if __name__ == '__main__':
    unittest.main()