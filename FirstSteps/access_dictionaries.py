# En esta parte del codigo veremos como acceder a los elementos de los diccionarios, para ello vamos a crear un diccionario con diferentes tipos de datos

country = {
    "capital" : "Madrid",
    "prefijo" : 34,
    "moneda" : "Euro",
    "poblacion" : 45000000,
    "idioma" : ["español", "gallego", "catalan", "euskera", "valenciano"],
}

print("La poblacion de España es de: ", country["poblacion"], " habitantes")

# Ahora vamos a ver la longitud de los elementos de los diccionarios, para ello vamos a utilizar la funcion len()

print("La longitud del diccionario es: ", len(country))# nos devuelve 5 elementos ya que son 5 elementos los que tiene el diccionario country que son capital, prefijo, moneda, poblacion e idioma

# Diccionarios Cambio de elementos, agregacion y eliminacion

# Cambio de elementos en un diccionario

shoes = {
    "marca" : "Nike",
    "modelo" : "Air Force 1",
    "talla" : 42,
    "color" : "blanco",
    "precio" : 100000,
    "tipo" : "zapatillas",
}

print("El diccionario shoes es: ", shoes)

shoes["precio"] = 120000 # Cambiamos el precio de las zapatillas
print("El diccionario shoes es: ", shoes)

# Agregacion de elementos en un diccionario

tv = {
    "marca" : "Samsung",
    "modelo" : "QLED",
    "sistema" : "Android",
    "pulgadas" : 55,
    "precio" : 1000000,
    "peso" : "20kg",
}

print("El diccionario tv es: ", tv)

tv["resolucion"] = "4K" # Agregamos la resolucion al diccionario tv

print("El diccionario tv es: ", tv)

# Eliminacion de elementos en un diccionario

phones = {
    "marca" : "Samsung",
    "modelo" : "Galaxy S20",
    "sistema" : "Android",
    "pulgadas" : 6.2,
    "precio" : 1000000,
    "peso" : "200g",
}

print("El diccionario phones es: ", phones)

del phones["sistema"] # Eliminamos el sistema del diccionario phones
print("El diccionario phones es: ", phones)