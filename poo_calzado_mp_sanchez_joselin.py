class Calzado:
    nombre: str
    def __init__(self, nombre: str):
        self.nombre = nombre

    def presentarse(self):
        print("Mi nombre de calzado es: ", self.nombre)
