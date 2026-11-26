print("==== CONTROL DE STOCK ====")
stock_texto = "diez"

try:
    stock = int(stock_texto)
    print(stock)
except ValueError:
    print("Error : debe ser numerico")
print("Fin del sistema")

"""
ValueError
TypeError
KeyError
IndexError
ZeroDivisionError
"""

def calcular_promedio_ventas(total, cantidad):
    try:
        resultado = total / cantidad
        return resultado
    except ZeroDivisionError:
        print("Error: Division entre cero")
        return None
    except TypeError:
        print("Error: valores deben ser numericos")
        return None

print("Caso 1: ", calcular_promedio_ventas(100, 4))
print("Caso 2: ", calcular_promedio_ventas(100, 0))
print("Caso 3: ", calcular_promedio_ventas(100, "cuatro"))


print("======= REVISION DE CAJA ========")
try:
    ventas = int(90)
    print("ventas", ventas)
except ValueError:
    print("Error de lectura")
else:
    print("revision completada")
finally:
    print("Cerrando revision")

def validar_descuento(descuento):
    if type(descuento) is not int:
        raise TypeError("El descuento debe ser un numero entero")
    if descuento < 0 or descuento > 100:
        raise ValueError("El descuento debe ser entre 0 y 100")
    return descuento


try:
    resultado = validar_descuento(-50)
    print("Descuento", resultado)
except (TypeError, ValueError) as error:
    print("Error: ", error)
