#OPERADORES
"""
Operadores aritmeticos
+ suma
- Resta
* Multiplicacion
/ Division
% Modulo
** Exponente
"""
valor1 = 10
valor2 = 3
suma = valor1 + valor2
resta = valor1 - valor2
multiplicacion = valor1 * valor2
division = valor1 / valor2
modulo = valor1 % valor2
exponente = valor1 ** valor2

print("Suma:", suma)
print("Resta:", resta)
print("Multiplicacion:", multiplicacion)
print("Division:", division)
print("Modulo:", modulo)
print("Exponente:", exponente)


print("Tabla de multiplicar del 5:")
multiplicador =5
print("5 x 1 = ", 5*1)
print("5 x 2 = ", 5*2)
print("5 x 3 = ", 5*3)
print("5 x 4 = ", 5*4)
print("5 x 5 = ", 5*5)
print("5 x 6 = ", 5*6)
print("5 x 7 = ", 5*7)
print("5 x 8 = ", 5*8)
print("5 x 9 = ", 5*9)
print("5 x 10 =", 5*10)


print("Area de un triangulo con base 5 y altura 10: ", (5*10)/2)

#OPERADORES DE COMPARACION 
"""
== igual
!= diferente
> mayor que
< menor que
>= mayor o igual que
<= menor o igual

"""

velocidad_anakin = 950
velocidad_sebula = 900

print("¿Anakin es mas rapido que sebula?", velocidad_anakin > velocidad_sebula)
print("¿Anakin es mas lento que sebula?", velocidad_anakin < velocidad_sebula)
print("¿Anakin es igual de rapido que sebula?", velocidad_anakin > velocidad_sebula)
print("¿Anakin es más diferente que Sebula?", velocidad_anakin != velocidad_sebula)
print("¿Anakin es más rápido o igual que Sebula?", velocidad_anakin >= velocidad_anakin)
print("¿Anakin es más lento o igual que Sebula?", velocidad_anakin<= velocidad_sebula)

#OPERADORES LOGICOS

"""
and
or
not
"""
motores = True
escudos = False
combustible = 80 

print("¿Todos los sistemas están funcionando?", motores and escudos)
print("¿Algunos sistemas están funcionando?", motores or escudos)
print("¿Los motores no están funcionando?", not motores)

cant_motores= 2
cant_alas = 4
combustible= 80 


print("¿La nave tiene al menos 2 motores y 4 alas?")
print(cant_motores >= 2 and cant_alas >= 4 and combustible >= 50 )
print("¿La nave tiene al menos 2 motores o 4 alas?")
print(cant_motores >= 2 and cant_alas >= 4 and combustible >= 50 )

print("¿La nave no tiene al menos 2 motores")
print( not cant_motores >= 2 and cant_alas >= 4 and combustible >= 50 )


#OPERADORES DE ASIGNACION
"""
- = (asignación)
- += (suma y asignación)
- -= (resta y asignación)
- *= (multiplicación y asignación)
- /= (división y asignación)
- %= (módulo y asignación)
- **= (potencia y asignación)
"""

velocidad = 100
print("Velocidad inicial:", velocidad)
velocidad += 50
print("Velocidad después de acelerar:", velocidad)
velocidad -= 30
print("Velocidad después de frenar:", velocidad)
multiplicador = 2
velocidad *= multiplicador
print("Velocidad después de multiplicar:", velocidad)
divisor = 4
velocidad /= divisor
print("Velocidad después de dividir:", velocidad)
modulo = 7
velocidad %= modulo
print("Velocidad después de aplicar módulo:", velocidad)
velocidad **= 2
print("Velocidad después de aplicar potencia:", velocidad)

# PRECEDENCIA DE OPERADORES 
"""
1. ()
2. ** (potencia)
3. * / % (multiplicación, división, módulo)
4. + - (suma, resta)
"""
resultado_1 = 10 + 5 * 2
print("Resultado 1:", resultado_1)
resultado_2 = (10+5)*2
print("Resultado 2:", resultado_2)
resultado_3 = 10 +5 *2 ** 2
print("Resultado 3: ", resultado_3)





