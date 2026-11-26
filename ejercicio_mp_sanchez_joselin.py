print("DESTINOS DE ENVIO")
print("Zona 1. Local (Quito)")
print("Zona 2. Resto del Ecuador")
print("Zona 3. Internacional")

peso_pedido = float(input("Ingresa el peso del pedido de zapatos en kilogramos: "))
zona_destino = int(input("Ingresa el numero de tu destino (1,2,3): "))

total = 0

if zona_destino == 1:
    total = peso_pedido * 5.0
elif zona_destino == 2:
    total = peso_pedido * 7.5
elif zona_destino == 3:
    total = peso_pedido * 10.0
else:
    print("Zona no valida")

print("Tu costo de envio es: ", total, "$")
