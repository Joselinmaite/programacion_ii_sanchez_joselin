# Condicional if
# Simple

stock = 10
if stock >= 10:
    print("Hay stock suficiente para vender")


#Condicional if-else
dinero_cliente = 100
precio_zapato = 150

if dinero_cliente >= precio_zapato:
    print("Puedes comprar el zapato")
else:
    print("No tienes suficiente dinero para comprar el zapato")

#if anidado

if dinero_cliente >= precio_zapato:
    print("Puedes comprar el zapato")
    if dinero_cliente > precio_zapato:
        print("Te sobra dinero")
    else:
        print("Tienes justo el dinero necesario")
else:
    print("No tienes suficiente dinero para comprar el zapato")

#Condicional if-elif-else

tipo_calzado = input("Ingresa el tipo de calzado (deportivo, formal, sandalia): ")
if tipo_calzado == "deportivo" and dinero_cliente >= precio_zapato:
    print("Puedes comprar el calzado deportivo")
elif tipo_calzado == "formal" and dinero_cliente >= precio_zapato:
    print("Puedes comprar el calzado formal")
elif tipo_calzado == "sandalia" and dinero_cliente >= precio_zapato:
    print("Puedes comprar la sandalia")
elif tipo_calzado in ("deportivo", "formal", "sandalia"):
    print("No te alcanza el dinero para este calzado")
else:
    print("Tipo de calzado no válido")
