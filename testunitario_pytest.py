from main import TransaccionPago
from main import Pago
from datetime import datetime

#TRANSACCION PAGO
def test_es_nombre_titular_string():
    assert TransaccionPago("Pedro Fernandez", 1234, "En espera").esNombreTitularString() == True


def test_es_nombre_cadena_vacia():
    assert TransaccionPago("Pedro Fernandez", 1234, "En espera").esNombreCadenaVacia() == False


def test_fecha_actual():
    assert TransaccionPago("Pedro Fernandez", 1234, "En espera").fechaActualTransaccion == datetime.today()


def test_es_nombre_alfabetico():
    assert TransaccionPago("Victor Nomberto", 1234, "En espera").esNombreAlfabetico() == True


def test_cuatro_digitos_tarjeta_transaccion():
    assert TransaccionPago("Pedro Fernandez", 1234, "En espera").cuatroDigitosTarjetaTransaccion() == True


def test_numero_transaccion_int():
    assert TransaccionPago("Pedro Fernandez", 1234, "En espera").numeroTransaccionInt() == True


#PAGO
def test_is_float():
    assert Pago("ASDF123456", 1234, 5000.22, "Pendiente").isfloat() == True


def test_tiene_ocho_digitos_codigo_pago():
    assert Pago("ASDF123456", 1234, 5000.22, "Pendiente").tieneOchoDigitosCodigoPago() == False


def test_codigo_contiene_solo_alfanumericos():
    assert Pago("ASDF123456", 1234, 5000.22, "Pendiente").codigoContieneSoloAlfanumericos() == True


def test_es_estado_pendiente():
    assert Pago("ASDF123456", 1234, 5000.22, "Pendiente").esEstadoPendiente() == True