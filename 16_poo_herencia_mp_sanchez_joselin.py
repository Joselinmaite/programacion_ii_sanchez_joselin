class Calzado:
    nombre: str
    def __init__(self, nombre: str):
        self.nombre = nombre

    def presentarse(self):
        print("Mi nombre de calzado es: ", self.nombre)


class Deportivo(Calzado):
    def __init__(self, nombre: str):
        super().__init__(nombre)

    def poner_en_oferta(self):
        print(self.nombre, "esta en oferta de temporada")


runner = Deportivo("Runner Pro")
runner.presentarse()
runner.poner_en_oferta()


class Producto:
    nombre: str
    stock: int

    def __init__(self, nombre: str, stock: int):
        self.nombre = nombre
        self.stock = stock

    def mostrar_stock(self):
        print("Producto:", self.nombre)
        print("Stock: ", self.stock)

class ProductoReabastecible(Producto):
    def __init__(self, nombre: str, stock: int):
        super().__init__(nombre, stock)

    def reabastecer(self, cantidad: int):
        if cantidad > 0:
            self.stock += cantidad

bota = ProductoReabastecible("Bota de cuero", 60)
print("=======ANTES DE REABASTECER========")
bota.mostrar_stock()
bota.reabastecer(100)
print("=====DESPUES DE REABASTECER========")
bota.mostrar_stock()
