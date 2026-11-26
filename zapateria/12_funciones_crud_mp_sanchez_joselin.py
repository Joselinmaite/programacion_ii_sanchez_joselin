inventario = [
    {"ZP-001": {
        "nombre": "Zapatilla deportiva",
        "stock": 80
        }
    },
    {
        "FM-002": {
        "nombre": "Zapato formal",
        "stock": 35
        }
    }

]

def crear_zapato(zapato):
    inventario.append(zapato)

def actualizar_zapato(zapato_actualizado, index):
    inventario[index].update(zapato_actualizado)


def leer_zapato(index):
    return inventario[index]

def eliminar_zapato(index):
    return inventario.pop(index)

print(inventario)
nuevo_zapato = {
        "SD-003": {
        "nombre": "Sandalia de verano",
        "stock": 80
        }
    }

crear_zapato(nuevo_zapato)
print(inventario)
zapato_actualizado = {
        "SD-006": {
        "nombre": "Sandalia de playa SD6",
        "stock": 85
        }
    }
actualizar_zapato(zapato_actualizado, 2)
print(inventario)
print(leer_zapato(2))
print(eliminar_zapato(2))
print(inventario)
