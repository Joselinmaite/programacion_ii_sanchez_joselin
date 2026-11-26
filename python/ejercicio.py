print("DESTINOS")
print("Zona 1. America")
print("Zona 2. Europa")
print("Zona 3. Resto de el mundo")

peso_paquete = float (input("Ingresa el peso de el paquete en killogramos: "))
zona_destino = int(input("Ingresa el numero de tu destino (1,2,3): "))

total = 0



if zona_destino == 1:
    total = peso_paquete * 5.0
elif zona_destino == 2:
    total = peso_paquete * 7.5
elif zona_destino == 3:
    total = peso_paquete * 10.0
else:
    print("no")

print("Tu costo final es: ", total,"$")               

