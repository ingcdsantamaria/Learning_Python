# Los diccionarios cuentan con los siguientes metodos:

# Metodos de actualizacion --> Estos metodos nos permiten actualizar el diccionario
#   * update() --> Actualiza el diccionario con los elementos del diccionario especificado (Actualizar y agregar elementos)

car = {
    "marca" : "Audi",
    "modelo" : "A4",
    "peso" : "1500kg",
    "motor" : "2.0 TDI",
    "año" : 2019,
    "precio" : 30000000,
}
print("El diccionario car es: ", car)
car.update({"año" : 2020}) # Actualizamos el año del diccionario car
print("El diccionario car es: ", car)


#   * setdefault() --> Devuelve el valor del elemento con la clave especificada. Si la clave no existe, inserte la clave, con el valor especificado

houses = {
    "tamano" : "100m2",
    "habitaciones" : 3,
    "baños" : 2,
    "garaje" : True,
    "jardin" : True,
    "precio" : 100000000,
    "ubicacion" : "Madrid",
}

print("El diccionario houses es: ", houses)

houses_var = houses.setdefault("garaje", False) # Devuelve True ya que el garaje es True, peor se preguntaran porque el valor no cambia a False, pues porque el valor ya existe y no se puede cambiar pero si se puede actualizar con el metodo update()
print("El valor de la clave garaje es: ", houses_var)

houses.setdefault("piscina", True) # Agregamos la piscina al diccionario houses, ya que no existe la clave piscina esto nos devuelve True, como podemos ver nos devuelve el valor de la clave piscina que es True actualizando el diccionario
print("El diccionario houses es: ", houses)

# Metodos de agregacion --> Estos metodos nos permiten agregar elementos al diccionario
#   * update() --> Actualiza el diccionario con los elementos del diccionario especificado

clouthes = {
    "tipo" : "camisa",
    "marca" : "Zara",
    "talla" : "M",
    "precio" : 200000,
    "color" : "blanco",
    "estampado" : "rayas",
    "material" : "algodon",
}

print("El diccionario clouthes es: ", clouthes)

#En caso de update() si la clave existe se actualiza el valor de la clave, pero tambien tiene una funcionalidad que es agregar elementos al diccionario, cuando la clave no existe

clouthes.update({"temporada" : "verano"}) # Agregamos la clave temporada al diccionario clouthes
print("El diccionario clouthes es: ", clouthes)

#   * setdefault() --> Devuelve el valor del elemento con la clave especificada. Si la clave no existe, inserte la clave, con el valor especificado

clouthes.setdefault("tipo de cuello", "camisero") # Agregamos la clave tipo de cuello al diccionario clouthes
print("El diccionario clouthes es: ", clouthes)

#   * fromkeys() --> Devuelve un diccionario con las claves y el valor especificados(recibe como parametros un iterable y un valor, devolviendo un diccionario con un mismo valor asignado a cada una de las claves, en caso de no ingresar ningun valor, va a devolver un valor vacio None)

keys = ("marca", "modelo", "precio", "color", "talla")
print("El diccionario keys es: ", keys)
keys = dict.fromkeys(keys) # Creamos un diccionario con las claves del diccionario clouthes
print("El diccionario keys es: ", keys)

# Metodos de eliminacion --> Estos metodos nos permiten eliminar elementos del diccionario
#   * pop() --> Elimina el elemento con la clave especificada

cell = {
    "marca" : "iphone",
    "modelo" : "11 pro",
    "capacidad" : "256GB",
    "ram" : "4GB",
    "batery" : "4000mAh",
    "precio" : 4000000,
}
print("El diccionario cell es: ", cell)

cell.pop("ram") # Eliminamos el elemento con la clave ram del diccionario cell

print("El diccionario cell es: ", cell)

#   * popitem() --> Elimina el ultimo elemento insertado

cell.popitem() # Eliminamos el ultimo elemento insertado del diccionario cell
print("El diccionario cell es: ", cell)

#   * clear() --> Elimina todos los elementos del diccionario

cell.clear() # Eliminamos todos los elementos del diccionario cell
print("El diccionario cell es: ", cell)

# Metodos de replicacion --> Estos metodos nos permiten replicar el diccionario
#   * copy() --> Devuelve una copia del diccionario

car = {
    "marca" : "Audi",
    "modelo" : "Q5",
    "peso" : "1500kg",
    "motor" : "2.0 TDI",
    "año" : 2022,
}
print("El diccionario car es: ", car)

car_copy = car.copy() # Creamos una copia del diccionario car
print("El diccionario car_copy es: ", car_copy)

# Metodos de busqueda --> Estos metodos nos permiten buscar elementos en el diccionario
#   * get() --> Devuelve el valor del elemento con la clave especificada

country = {
    "nombre" : "Colombia",
    "capital" : "Bogota",
    "prefijo" : "+57",
    "moneda" : "peso colombiano",
    "idioma" : "español",
    "poblacion" : 50000000,
}

print("El diccionario country es: ", country)
print("El valor de la clave nombre es: ", country.get("nombre")) # Devuelve el valor de la clave nombre

#   * items() --> Devuelve una lista que contiene una tupla para cada par clave-valor

print("El diccionario country es: ", country)
print("El diccionario country es: ", country.items()) # Devuelve una lista que contiene una tupla para cada par clave-valor

#   * keys() --> Devuelve una lista que contiene las claves del diccionario

print("El diccionario country es: ", country)
print("El diccionario country es: ", country.keys()) # Devuelve una lista que contiene las claves del diccionario

#   * values() --> Devuelve una lista de todos los valores del diccionario

print("El diccionario country es: ", country)
print("El diccionario country es: ", country.values()) # Devuelve una lista de todos los valores del diccionario