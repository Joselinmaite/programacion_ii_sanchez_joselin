# string cadenas de caracteres
vendedor = "Ana Torres"
cliente = "Lucia Paredes"
marca = "Nike"
ciudad = "Quito"
codigo = "327"

print("El vendedor es : " + vendedor)
print("El vendedor", type(vendedor))
print("El cliente es : " + cliente)
print("El cliente", type(cliente))
print("La marca es : " + marca)
print("La marca", type(marca))
print("La ciudad es : " + ciudad)
print("La ciudad", type(ciudad))
print("El codigo es : " + codigo)
print("El codigo", type(codigo))

longitud_vendedor = len(vendedor)
print("La longitud del nombre del vendedor es: " + str(longitud_vendedor))

longitud_cliente = len(cliente)
print("La longitud del nombre del cliente es: " + str(longitud_cliente))


mensaje = "La zapateria ha lanzado una oferta en calzado deportivo."
print("El mensaje es: " + mensaje)
mensaje_mayusculas = mensaje.upper()
print("El mensaje en mayusculas es: " + mensaje_mayusculas)
mensaje_minusculas = mensaje.lower()
print("El mensaje en minusculas es: " + mensaje_minusculas)

comunicado = "Las ofertas son validas en Quito."
print("El comunicado es: " + comunicado)
nuevo_comunicado = comunicado.replace("Quito", "Guayaquil")
print("El nuevo comunicado es: ", nuevo_comunicado)

sucursales = "Quito, Guayaquil, Cuenca, Ambato"
sucursales_lista = sucursales.split(", ")
print(sucursales_lista)
print("La lista de sucursales es: " + str(sucursales_lista))

codigo_producto = "ZP-101"
print("El codigo del producto es: " + codigo_producto)
print("El primer caracter del codigo es: " + codigo_producto[0])
print("El segundo caracter del codigo es: " + codigo_producto[1])
print("El tercer caracter del codigo es: " + codigo_producto[2])
print("El cuarto caracter del codigo es: " + codigo_producto[3])
print("El quinto caracter del codigo es: " + codigo_producto[4])
print("El sexto caracter del codigo es: " + codigo_producto[-1])

ciudad = "      Quito    "
print("La ciudad es: " + ciudad)
print("La ciudad sin espacios es: " + ciudad.strip())
