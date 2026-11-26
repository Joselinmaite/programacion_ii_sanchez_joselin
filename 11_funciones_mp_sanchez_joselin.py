#FUNCIONES
def abrir_tienda():
    print("== zapateria Pasos Firmes ==")
    print("Sistema de caja activado")
abrir_tienda()

#FUNCIONES CON PARAMETRO
def saludar_cliente(nombre):
    print(f"Bienvenido a la zapateria: {nombre}")

saludar_cliente("Lucia Paredes")
saludar_cliente("Luis Andrade")

def mostrar_zapato(nombre, stock):
    print(f"zapato:{nombre}")
    print(f"cantidad en stock: {stock}")
mostrar_zapato("Zapatilla deportiva", 80)

#funciones que devuelven dato o informacion
#return

def calcular_stock(inicial, vendidos):
    restante = inicial - vendidos
    return restante
resultado = calcular_stock(100, 25)
print(f"Stock: {resultado}")

def hay_stock(stock):
    return stock > 0

if hay_stock(80):
    print("Producto disponible para la venta")
else:
    print("Producto necesita reabastecimiento")
