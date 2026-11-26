"""
Control de inventario de la zapateria
"""

productos = [
    {
        "nombre": "Zapatilla deportiva",
        "stock": 80,
        "tallas": ["38", "40", "42"]
    },
    {
        "nombre": "Zapato formal",
        "stock": 35,
        "tallas": ["41"]
    },
    {
        "nombre": "Sandalia",
        "stock": 65,
        "tallas": ["36", "37"]
    }
]

productos_listos = 0
productos_reabastecidos = 0
total_tallas = 0
total_ciclos = 0
for numero, producto in enumerate(productos, start=1):
    print(f"---Producto : {numero}-{producto}")
    if producto["stock"] >= 50:
        print("Estado inicial: Listo")
        productos_listos += 1
    else:
        print("Estado inicial: Reabastecer")
        productos_reabastecidos += 1
        ciclo = 0
        while producto["stock"] < 50:
            ciclo += 1
            producto["stock"] += 10
        total_ciclos += ciclo
        print("Reabastecimiento completado")
        print("Estado final: Listo")

    total_tallas += len(producto["tallas"])
    for talla in producto["tallas"]:
        print(f"talla: {talla}")


print("========================")
print("RESUMEN")
print("========================")
print(f"Total productos: {len(productos)}")
print(f"Productos listos inicialmente: {productos_listos}")
print(f"Productos reabastecidos: {productos_reabastecidos}")
print(f"Total tallas: {total_tallas}")
print(f"Total ciclos: {total_ciclos}")
