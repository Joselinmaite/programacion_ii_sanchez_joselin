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


print("Tabla de multiplicar del 5 (cajas de 5 pares):")
multiplicador = 5
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


print("Area de una etiqueta triangular con base 5 y altura 10: ", (5*10)/2)

#OPERADORES DE COMPARACION
"""
== igual
!= diferente
> mayor que
< menor que
>= mayor o igual que
<= menor o igual

"""

precio_nike = 95
precio_adidas = 90

print("¿Nike es mas caro que Adidas?", precio_nike > precio_adidas)
print("¿Nike es mas barato que Adidas?", precio_nike < precio_adidas)
print("¿Nike cuesta igual que Adidas?", precio_nike == precio_adidas)
print("¿Nike tiene un precio diferente a Adidas?", precio_nike != precio_adidas)
print("¿Nike es mas caro o igual que Adidas?", precio_nike >= precio_adidas)
print("¿Nike es mas barato o igual que Adidas?", precio_nike <= precio_adidas)

#OPERADORES LOGICOS

"""
and
or
not
"""
caja_abierta = True
sistema_facturacion = False
stock = 80

print("¿Todo funciona en la tienda?", caja_abierta and sistema_facturacion)
print("¿Algo funciona en la tienda?", caja_abierta or sistema_facturacion)
print("¿La caja no esta abierta?", not caja_abierta)

cant_vendedores = 2
cant_cajas = 4
stock = 80


print("¿La tienda tiene al menos 2 vendedores y 4 cajas de zapatos?")
print(cant_vendedores >= 2 and cant_cajas >= 4 and stock >= 50)
print("¿La tienda tiene al menos 2 vendedores o 4 cajas de zapatos?")
print(cant_vendedores >= 2 or cant_cajas >= 4)

print("¿La tienda no tiene al menos 2 vendedores?")
print(not cant_vendedores >= 2)


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

ventas = 100
print("Ventas iniciales:", ventas)
ventas += 50
print("Ventas después de un buen día:", ventas)
ventas -= 30
print("Ventas después de devoluciones:", ventas)
multiplicador = 2
ventas *= multiplicador
print("Ventas después de multiplicar:", ventas)
divisor = 4
ventas /= divisor
print("Ventas después de dividir:", ventas)
modulo = 7
ventas %= modulo
print("Ventas después de aplicar módulo:", ventas)
ventas **= 2
print("Ventas después de aplicar potencia:", ventas)

# PRECEDENCIA DE OPERADORES
"""
1. ()
2. ** (potencia)
3. * / % (multiplicación, división, módulo)
4. + - (suma, resta)
"""
resultado_1 = 10 + 5 * 2
print("Resultado 1:", resultado_1)
resultado_2 = (10 + 5) * 2
print("Resultado 2:", resultado_2)
resultado_3 = 10 + 5 * 2 ** 2
print("Resultado 3: ", resultado_3)
