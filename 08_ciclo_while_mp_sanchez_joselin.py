stock = 100
ronda = 1

while stock >= 20:
    print(f"ronda de venta {ronda}")
    print(f"Stock inicial: {stock}")

    stock -= 20
    print(f"Stock restante: {stock}")
    ronda += 1
print("Venta finalizada")
