print("==== CONTROL DE ENERGIA ====")
energia_texto="ochenta"

try:
   energia=int(energia_texto)
   print(energia)
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

def calcular_energia(total,cantidad):
    try:
        resultado= total / cantidad
        return resultado
    except ZeroDivisionError:
        print("Error: Division entre cero")
        return None
    except TypeError:
        print("Error: valores deben ser numericos")
        return None

print("Caso 1: ", calcular_energia(100,4))
print("Caso 2: ", calcular_energia(100,0))
print("Caso 3: ", calcular_energia(100,"cuatro"))


print("======= DIAGNOTICO R2-D2 ========")
try:
    energia=int(90)
    print("energia", energia)
except ValueError:
    print("Error de lectura")
else:    
    print("diagnostico completado")
finally:
    print("Cerrando diagnostico")   

def vallidar_energia(energia):
    if type(energia) is not int:
        raise TypeError("La energia debe ser un numero entero")
    if energia <0 or energia >100:
        raise TypeError("La energia debe ser entre 0 y 100")
    return energia


try:
    resultado = vallidar_energia(-50)
    print("Energia", resultado)
except(TypeError, ValueError) as error:
    print("Error: ", error)   
             
         