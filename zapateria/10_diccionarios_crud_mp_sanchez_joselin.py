zapatos = [
    {
        "codigo": "ZP-001",
        "modelo": "Deportivo",
        "stock": 90,
        "activo": True
    },

    {
        "codigo": "ZP-002",
        "modelo": "Deportivo",
        "stock": 40,
        "activo": False
    },

    {
        "codigo": "FM-001",
        "modelo": "Formal",
        "stock": 80,
        "activo": True
    },

]

cantidad_zapatos = len(zapatos)
print(cantidad_zapatos)

nuevo_zapato = {
    "codigo": "ZP-004",
    "modelo": "Deportivo",
    "stock": 100,
    "activo": True
}

#CRUD
#CREATE
zapatos.append(nuevo_zapato)
print(len(zapatos))
print(zapatos)

#READ
zapato = zapatos[0]

print(f"Codigo:{zapato['codigo']}")
print(f"Modelo:{zapato['modelo']}")
print(f"Stock:{zapato['stock']}")
print(f"Activo:{zapato['activo']}")

#UPDATE
zapato = zapatos[2]
zapato["codigo"] = "FM-002"
zapato["stock"] = 85
zapato["activo"] = False
print(f"zapatos:{zapatos}")
#DELETE
eliminado = zapatos.pop(2)
print(f"zapatos: {zapatos}")
