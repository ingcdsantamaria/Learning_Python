# Ahora hablaremos del for que hace parte de los ciclos, el for es un ciclo que nos permite ejecutar un bloque de codigo un numero determinado de veces, el for se puede usar con listas, tuplas, diccionarios, cadenas de texto y rangos

# * Es una estructura de control cíclica que se ejecutar una o varias veces, dependiendo de la cantidad de elementos que tenga un objeto iterable.
# * El for se puede usar para recorrer los elementos de un objeto iterable, como una lista, una tupla, un diccionario, un conjunto, un rango, etc.
# * Esta conformado por:
#     * La palabra reservada for
#     * Una variable que va a tomar el valor de cada elemento del objeto iterable o valor inicial
#     * La palabra reservada in
#     * El objeto iterable
#     * Dos puntos

# Aplicando FOR en strings
for letter in "Hola":# En este caso letter es la variable que va a tomar el valor de cada letra de la palabra Hola y lo que hace es recorrer cada letra de la palabra Hola
    print(letter)

# Aplicando FOR en listas
languages = ["Python", "Java", "JavaScript", "PHP", "C#", "C++", "Ruby", "Kotlin", "Go", "Swift", "Rust", "Scala", "Perl", "R", "Dart", "TypeScript", "Julia", "Haskell", "Elixir", "Clojure", "F#"]

for language in languages:# En este caso language es la variable que va a tomar el valor de cada elemento de la lista languages y lo que hace es recorrer cada elemento de la lista languages mientras que la variable language tome el valor de cada elemento de la lista languages
    print(language)

# Aplicando FOR en tuplas
brand = ("Nike", "Reebok", "Guess", "Hugo Boss")

for i in brand:# En este caso i es la variable que va a tomar el valor de cada elemento de la tupla brand y lo que hace es recorrer cada elemento de la tupla brand mientras que la variable i tome el valor de cada elemento de la tupla brand
    print(i)

# Aplicando FOR en diccionarios
city = {
    "nombre": "Medellin",
    "departamento": "Antioquia",
    "pais": "Colombia",
    "distrito": "Valle de Aburra",
    "altitud": "1.495 msnm",
}

for key in city:# En este caso key es la variable que va a tomar el valor de cada clave del diccionario city y lo que hace es recorrer cada clave del diccionario city mientras que la variable key tome el valor de cada clave del diccionario city
    print(key)

# ahora iteramos sobre los valores del diccionario
for value in city.values():# En este caso value es la variable que va a tomar el valor de cada valor del diccionario city y lo que hace es recorrer cada valor del diccionario city mientras que la variable value tome el valor de cada valor del diccionario city
    print(value)

# Ahora iteramos ambos elementos del diccionario
for key, value in city.items():# En este caso key es la variable que va a tomar el valor de cada clave del diccionario city y value es la variable que va a tomar el valor de cada valor del diccionario city y lo que hace es recorrer cada clave y valor del diccionario city mientras que la variable key tome el valor de cada clave del diccionario city y la variable value tome el valor de cada valor del diccionario city
    print(key, ":", value)

# Aplicando FOR en sets (Pendiente de edicion)
# Aplicando FOR en rangos (Pendiente de edicion)

#--------------------------------------------------------------------------------#

# Ahora hablaremos de las sentencias break, continue y pass

# La sentencia break se utiliza para terminar un ciclo, es decir, si se cumple una condicion se termina el ciclo, la sentencia break se puede usar en los ciclos for y while

for i in "Hola - Mundo":# En este caso i es la variable que va a tomar el valor de cada letra de la palabra Hola - Mundo y lo que hace es recorrer cada letra de la palabra Hola - Mundo mientras que la variable i tome el valor de cada letra de la palabra Hola - Mundo
    if i == "M":# En este caso si la variable i toma el valor de la letra M se termina el ciclo
        break
    print(i)

# La sentencia continue se utiliza para saltar una iteracion, es decir, si se cumple una condicion se salta la iteracion, la sentencia continue se puede usar en los ciclos for y while

listPets = ["Perro", "Tortuga", "Gato", "Loro", "Conejo", "Hamster", "Pez"]

for i in listPets:# En este caso i es la variable que va a tomar el valor de cada elemento de la lista listPets y lo que hace es recorrer cada elemento de la lista listPets mientras que la variable i tome el valor de cada elemento de la lista listPets
    if i == "Tortuga":# En este caso si la variable i toma el valor de la palabra Tortuga se salta la iteracion
        continue
    print(i)

# La sentencia pass se utiliza para dejar un bloque de codigo vacio, es decir, si se cumple una condicion se deja un bloque de codigo vacio, la sentencia pass se puede usar en los ciclos for y while

dictColor = {
    "rojo" : 1,
    "verde" : 2,
    "azul" : 3,
    "amarillo" : 4,
    "blanco" : 5,
    "negro" : 6,
}

for i in dictColor:
    if i == "rojo":
        pass
    print(i)