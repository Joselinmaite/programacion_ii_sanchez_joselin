
zapatos = [
    "Zapatilla deportiva",
    "Zapato formal",
    "Sandalia"
]


for zapato in zapatos:
    print("Inspeccionando", zapato)
print("Inspeccion realizada")

rondas = range(1, 6)
print("Tipo de Rondas: ", type(rondas))
for ronda in rondas:
    print(f"Ronda de inventario: {ronda}")
    print(f"Tipo de dato ronda: {type(ronda)}")

cajas = range(1, 17, 3)
print("Tipo de Cajas: ", type(cajas))
for caja in cajas:
    print(f"Revisar: caja Z-{caja}")
    print(f"Tipo de dato caja: {type(caja)}")

marcas = [
    "Nike",
    "Adidas",
    "Puma"
]

recorrido = enumerate(marcas, start=1)

for posicion, marca in recorrido:
    print(f"Marca {posicion}: {marca}")
    print(f"Tipos de dato {type(posicion)}: {type(marca)}")



sucursales = [
    "Quito",
    "Guayaquil",
    "Cuenca",
    "Ambato",
    "Loja"

]

for sucursal in sucursales:
    if sucursal == "Cuenca":
        continue
    if sucursal == "Ambato":
        break
    print(f"Sucursal visitada: {sucursal}")


cliente = {}
cliente_activo = {
    "nombre": "Lucia",
    "puntos": 120,
    "estilo_preferido": "Deportivo",
    "compras": ["zapatillas running", "botas de cuero", "sandalias de verano"],
    "descripcion": {
        "talla": 38,
        "genero": "femenino"
    }
}

print(cliente_activo)
zapato = dict(modelo="AZ-1", stock=8, descuento=2)
print(zapato)

cliente["nombre"] = "Luis"
cliente["puntos"] = 150
print(cliente)

for clave, valor in cliente_activo.items():
    print(f"{clave} - {valor}")
