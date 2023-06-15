#En python encontramos diferentes tipos de datos en este caso hablasemos de los mas usados:

# 1. String (cadenas de texto)
course_name = "Curso de Python"
#si queremos que se imprima en la consola el texto con comillas debemos usar comillas simples
message = "'Hola mundo'"
#si queremos hacer un salto de linea hay 4 formas de hacelo
# 1.1. Usando \n
message = "Hola mundo \nAdios mundo"
# 1.2. Usando """ """
message = """
Hola mundo
Adios mundo
"""
# 1.3. haciendo lo desde el print
print(message + "\n" + "Adios mundo")
# 1.4. Usando \t realiza un tabulador
message = "Hola mundo \tAdios mundo"
print(message)

# 2. Int (enteros)
number = 3
# 2.1. Podemos tambien imprimir numeros negativos
number = -3
print(number)

# 3. Float (decimales)
float_number = -3.53
float_number = 3.53
print(float_number)

# 4. Bool (verdadero o falso)
boolean = True
false_boolean = False
print(boolean)
print(false_boolean)

#si queremos saber en realidad que typo de dato es utilizamos type()
print(type(course_name))
print(type(number))
print(type(float_number))
print(type(boolean))

#En este archivo hablaremos de las listas las cuales pueden almacenar diferentes tipos de datos(enteros, flotantes, cadenas, booleanos, etc)
#Las listas estan representadas por corchetes y los elementos de la lista estan separados por comas []

#Sintaxis de una listas
list1 = [12, "martes", False, "viernes", -200.78]
print(list1)
print(type(list1))

list2 = ["venus", "tierra", "marte", "jupiter", "saturno", "urano", "neptuno", "pluton"]
print(list2)
print(type(list2))


#Listas, que es una lista, una lista es una estructura de datos que nos permite organizar elementos de manera secuencial, es decir, uno detras de otro, en python las listas pueden guardar diferentes tipos de datos, por ejemplo:

# 1. List
# 1.1. Podemos crear una lista vacia
my_list = []
# 1.2. Podemos crear una lista con datos
my_list = [1, 2, 3]
# 1.3. Podemos crear una lista con datos de diferentes tipos
my_list = [1, "Hello", 3.4, True]
# 1.4. Podemos crear una lista con datos de diferentes tipos y dentro de ella podemos crear otra lista
my_list = [1, "Hello", 3.4, True, [1, 2, 3]]
# 1.5. Podemos crear una lista con datos de diferentes tipos y dentro de ella podemos crear otra lista y dentro de esa lista podemos crear otra lista
my_list = [1, "Hello", 3.4, True, [1, 2, 3, [1, 2, 3]]]
# podemos ver el tipo de lista que es con type() y imprimirlo en consola con print()
print(type(my_list))
print(my_list)
# que operaciones nos permite hacer una lista en python, nos permite agregar elementos, eliminar elementos, ordenar elementos, buscar elementos, etc, esto lo veremos mas adelante

#tuple, que es una tupla, una tupla es una estructura de datos que nos permite organizar elementos de manera secuencial, es decir, uno detras de otro, en python las tuplas pueden guardar diferentes tipos de datos, por ejemplo:
# 1. Tuple

# Una tupla en si es una lista que no se puede agregar ni eliminar elementos, es decir, es inmutable
# Se puede representar con parentesis o sin parentesis ()
# Para acceder a un elemento se realiza mediante el indice, el indice empieza desde 0

#Sintaxis de una tupla
#Con parentesis
tuple1 = (1, 2, 3, 4, 5)
print(tuple1)
print(type(tuple1))

#Sin parentesis
tuple2 = "perro", "gato", "loro"
print(tuple2)
print(type(tuple2))

# 1.1. Podemos crear una tupla vacia
my_tuple = ()
# 1.2. Podemos crear una tupla con datos
my_tuple = (1, 2, 3)
# 1.3. Podemos crear una tupla con datos de diferentes tipos
my_tuple = (1, "Hello", 3.4, True)
# 1.4. Podemos crear una tupla con datos de diferentes tipos y dentro de ella podemos crear otra tupla
my_tuple = (1, "Hello", 3.4, True, (1, 2, 3))
# 1.5. Podemos crear una tupla con datos de diferentes tipos y dentro de ella podemos crear otra tupla y dentro de esa tupla podemos crear otra tupla
my_tuple = (1, "Hello", 3.4, True, (1, 2, 3, (1, 2, 3)))
# podemos ver el tipo de tupla que es con type() y imprimirlo en consola con print()
print(type(my_tuple))
print(my_tuple)
# la gran diferencia entre una tupla y una lista es que la tupla es inmutable, es decir, no podemos modificarla, no podemos agregarle elementos, no podemos eliminar elementos, no podemos ordenarla, no podemos buscar elementos, etc, a diferencia de la lista que si podemos hacer todas estas operaciones, esto lo veremos mas adelante

#diccionarios, que es un diccionario, un diccionario es una estructura de datos que nos permite organizar elementos de manera NO secuencial, es decir, no es uno detras de otro, en python los diccionarios pueden guardar diferentes tipos de datos, por ejemplo:
# 1. Dictionary
# 1.1. Podemos crear un diccionario vacio
my_dictionary = {}
# 1.2. Podemos crear un diccionario con datos
my_dictionary = {"Eduardo": 1, "Juan": 2, "Pedro": 3}
# 1.3. Podemos crear un diccionario con datos de diferentes tipos
my_dictionary = {"Eduardo": 1, "Juan": "Hello", "Pedro": 3.4}
# 1.4. Podemos crear un diccionario con datos de diferentes tipos y dentro de ella podemos crear otro diccionario
my_dictionary = {"Eduardo": 1, "Juan": "Hello", "Pedro": 3.4, "Maria": {"Eduardo": 1, "Juan": "Hello", "Pedro": 3.4}}
# podemos ver el tipo de diccionario que es con type() y imprimirlo en consola con print()
print(type(my_dictionary))
print(my_dictionary)
# que operaciones nos permite hacer un diccionario en python, nos permite agregar elementos, eliminar elementos, ordenar elementos, buscar elementos, etc, esto lo veremos mas adelante
# la diferencia entre el dicicionario, tuplas y listas es que el diccionario es una estructura de datos que nos permite organizar elementos de manera NO secuencial, es decir, no es uno detras de otro, a diferencia de la lista y la tupla que si son elementos de manera secuencial, esto lo veremos mas adelante

#range, que es un rango, un rango es una estructura de datos que nos permite organizar elementos de manera secuencial, es decir, uno detras de otro, en python los rangos pueden guardar diferentes tipos de datos, por ejemplo:
# 1. Range
# 1.1. Podemos crear un rango con datos
my_range = range(1, 10)
# 1.2. Podemos crear un rango con datos de diferentes tipos
my_range = range(1, 10, 2)
#incluso podemos crear un rango 20
my_range = range(20)
# un rango dentro de una lista
my_range = list(range(20))
# podemos ver el tipo de rango que es con type() y imprimirlo en consola con print()
print(type(my_range))
print(my_range)

#set (conjunto), que es un conjunto, un conjunto es una estructura de datos que nos permite organizar elementos de manera secuencial, es decir, uno detras de otro, en python los conjuntos pueden guardar diferentes tipos de datos, por ejemplo:
# 1. Set
# 1.1. Podemos crear un conjunto con datos como de animales
my_set = {"Perro", "Gato", "Leon"}
var_st = set(my_set)
print(var_st)
# que operaciones nos permite hacer un conjunto en python, nos permite agregar elementos, eliminar elementos, ordenar elementos, buscar elementos, etc, esto lo veremos mas adelante
# la diferencia entre el conjunto, dicicionario, tuplas y listas es que el conjunto es una estructura de datos que nos permite organizar elementos de manera secuencial, es decir, uno detras de otro, a diferencia del diccionario que es una estructura de datos que nos permite organizar elementos de manera NO secuencial, es decir, no es uno detras de otro, a diferencia de la lista y la tupla que si son elementos de manera secuencial, esto lo veremos mas adelante