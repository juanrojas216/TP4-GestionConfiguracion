from datetime import datetime


class TransaccionPago:

    # CONSTRUCTOR
    def __init__(self, nombreTitularTransaccion, digitosTarjetaTransaccion, estadoTransaccion):
        self.nombreTitularTransaccion = nombreTitularTransaccion
        self.digitosTarjetaTransaccion = digitosTarjetaTransaccion
        self.fechaActualTransaccion = datetime.today()
        self.estadoTransaccion = estadoTransaccion

    # NACHO
    def esNombreTitularString(self):
        return isinstance(self.nombreTitularTransaccion, str)

    # NACHO
    def esNombreCadenaVacia(self):
        if len(self.nombreTitularTransaccion) == 0:
            return True
        else:
            return False

    # NACHO
    def fechaActual(self):
        return self.fechaActualTransaccion

    # SARA
    def esNombreAlfabetico(self):
        return self.nombreTitularTransaccion.replace(" ", "").isalpha()

    # SARA
    def cuatroDigitosTarjetaTransaccion(self):
        if len(str(self.digitosTarjetaTransaccion)) == 4: return True

    # JULI
    def numeroTransaccionInt(self):
        return str(self.digitosTarjetaTransaccion).isnumeric()


class Pago:
    # clientePago: aca va la instancia de cliente

    # Constructor
    def __init__(self, codigoPago, nroFactura, montoPago, estadoPago):
        self.codigoPago = codigoPago
        self.nroFactura = nroFactura
        self.montoPago = montoPago
        self.estadoPago = estadoPago
        self.fechaCreacionPago = datetime.today()

    # FRANQUITO SPIDER
    def isfloat(self):
        try:
            float(self.montoPago)
            return True
        except ValueError:
            return False

    # FRANQUITO SPIDER
    def tieneOchoDigitosCodigoPago(self):
        if (len(self.codigoPago) == 8):
            return True
        else:
            return False

    # JUN
    def codigoContieneSoloAlfanumericos(self):
        return self.codigoPago.isalnum()

    def esEstadoPendiente(self):
        if (self.estadoPago == "Pendiente"): return True
