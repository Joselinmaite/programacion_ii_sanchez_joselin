class Zapato:
    nombre: str
    precio: float
    stock: int

    def __init__(self, nombre: str, precio: float, stock: int):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def saludar(self):
        print("Hola, soy el zapato: ", self.nombre)

    def reabastecer(self):
        aumento = 20
        self.stock += aumento

    def vender(self, cantidad):
        if cantidad <= self.stock:
            self.stock -= cantidad
            total = self.precio * cantidad
            print("Venta de", self.nombre, "por un total de", total)
        else:
            print("No hay stock suficiente de", self.nombre)

zapatilla = Zapato("Zapatilla Runner", 89.99, 50)
zapatilla.saludar()

print("Nombre del zapato: ", zapatilla.nombre)
print("Stock del zapato: ", zapatilla.stock)
zapatilla.reabastecer()
print("Stock del zapato: ", zapatilla.stock)
zapatilla.vender(3)
print("Stock del zapato: ", zapatilla.stock)
