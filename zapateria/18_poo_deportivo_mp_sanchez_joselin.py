from poo_calzado_mp_sanchez_joselin import Calzado

class Deportivo(Calzado):
    def __init__(self, nombre: str):
        super().__init__(nombre)

    def poner_en_oferta(self):
        print(self.nombre, "esta en oferta de temporada")


runner = Deportivo("Runner Pro")
runner.presentarse()
runner.poner_en_oferta()
