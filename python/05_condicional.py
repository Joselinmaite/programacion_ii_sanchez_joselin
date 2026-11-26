# Condicional if
# Simple

combustible = 10
if combustible >= 10:
    print("Puedes despegar")


#Condicional if-else
creditos = 100
precio_repuesto = 150

if creditos >= precio_repuesto:
    print("Puedes comprar el repuesto")
else:
    print("No tienes suficientes creditos para comprar el repuesto")

#if anidado

if creditos >= precio_repuesto:
    print("Puedes comprar el repuesto")
    if creditos > precio_repuesto:
        print("Te sobran creditos")
    else:
        print("Te quedas justo con los creditos necesarios")
else:
    print("No tienes suficientes creditos para comprar el repuesto")

#Condicional if-elif-else



tipo_repuesto = input("Ingresa el tipo de repuesto (motor, ala, escudo): ")
if tipo_repuesto == "motor" and creditos >= precio_repuesto and tipo_repuesto == "ala":
    print("Puedes comprar el repuesto y te sobran créditos")
elif tipo_repuesto == "ala" and creditos >= precio_repuesto:
    print("Puedes comprar el repuesto y te sobran créditos")
elif tipo_repuesto == "escudo" and creditos >= precio_repuesto:
    print("Puedes comprar el repuesto y te sobran créditos")
else:
    print("Tipo de repuesto no válido")