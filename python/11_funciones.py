#FUNCIONES
def activas_sistema():
    print("== sistema de naboo ==")
    print("Sistema de control activado")
activas_sistema()

#FUNCIONES CON PARAMETRO
def saludar_jedi(nombre):
    print(f"Que la fuerza te acompañe: {nombre}")

saludar_jedi("Qui-Gon Jim")
saludar_jedi("Obi-Wan Kenobi")

def mostrar_nave(nombre, combustible):
    print(f"nave:{nombre}")
    print(f"cantidad combustible: {combustible}")
mostrar_nave("Caza N-1", 80)

#funciones que devuelven dato o informacion
#return

def calcular_combustible(inicial, consumo):
    restante=inicial - consumo
    return restante
resultado =calcular_combustible(100,25)
print(f"Combustible: {resultado}")

def nave_preparada(combustible):
    return combustible

if nave_preparada(80):
    print("Nave autorizada para despegar")
else:
    print("Nave necesita recarga")    
