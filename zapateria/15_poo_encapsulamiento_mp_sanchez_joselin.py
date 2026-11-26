class Zapato:
    nombre: str
    _precio_costo: float

    def __init__(self, nombre: str, precio_costo: float):
        self.nombre = nombre
        self._precio_costo = precio_costo

    def get_precio_costo(self):
        return self._precio_costo

zapatilla = Zapato("Zapatilla Runner", 45.50)
print("Zapato: ", zapatilla.nombre)
print("Precio de costo: ", zapatilla.get_precio_costo())

class CajaTienda:
    cajero: str
    _saldo: int

    def __init__(self, cajero: str, saldo: int):
        self.cajero = cajero
        self._saldo = saldo

    def get_saldo(self):
        return self._saldo

    def retirar_dinero(self, cantidad: int):
        if cantidad > 0 and cantidad <= self._saldo:
            self._saldo -= cantidad
            print("Retiro realizado", cantidad)
        else:
            print("Retiro no permitido")


caja = CajaTienda("Ana Torres", 5000)
print("Cajero: ", caja.cajero)
print("Saldo inicial", caja.get_saldo())
caja.retirar_dinero(500)
print("Saldo final", caja.get_saldo())
