from 17 poo guerrero import Guerrero

class Saiyajin(Guerrero):
    def _init_(self, nombre:str):
        super().init_(nombre)

    def transformarse(self):
        print(self.nombre, "Se transforma en Super Saiyajin")


goku = Saiyajin("Goku")
goku.presentarse()
goku.transformarse()  