#En este archivo hablaremos sobre los metodos de las listas como metodos de replicacion, metodos de agregacion, metodos de eliminacion, metodos de ornamiento

# 1) Metodos de agregacion: este metodo nos permite agregar elementos a una lista, estos metodos son los siguientes:
# * append(): este metodo nos permite agregar un elemento al final de la lista
# * extend(): este metodo nos permite agregar varios elementos al final de la lista
# * insert(): este metodo nos permite agregar un elemento en una posicion especifica de la lista

# 2) Metodos de replicacion: este metodo nos permite replicar una lista, estos metodos son los siguientes:
# * copy(): este metodo nos permite replicar una lista

# 3) Metodos de eliminacion: este metodo nos permite eliminar elementos de una lista, estos metodos son los siguientes:
# * remove(): este metodo nos permite eliminar un elemento de la lista
# * pop(): este metodo nos permite eliminar un elemento de la lista por posicion
# * clear(): este metodo nos permite eliminar todos los elementos de la lista

# 4) Metodos de ordenamiento: este metodo nos permite ordenar los elementos de una lista, estos metodos son los siguientes:
# * sort(): este metodo nos permite ordenar los elementos de una lista de forma ascendente
# * reverse(): este metodo nos permite ordenar los elementos de una lista de forma descendente

# Acontinuacion veremos los metodos de las listas
# --------------------------------------------Metodos de agregacion--------------------------------------------
#Este metodo nos permite agregar elementos a una lista, estos metodos son los siguientes:

# 1) append() --> este metodo nos permite agregar un elemento al final de la lista
list1 = ["leon", "tigre", "jaguar", "pantera", "puma", "leopardo", "guepardo", "leopardo de las nieves", "leopardo de las nieves"]
print("Lista original: ", list1)
list1.append("leon de montaña")
print("Lista agregada: ", list1)

# 2) extend() --> este metodo nos permite agregar varios elementos al final de la lista
list_1 = ["Alemania", "España", "Francia", "Italia", "Portugal", "Inglaterra", "Holanda", "Belgica", "Suiza", "Austria"]
list_2 = ["China", "India", "Afganistan"]
print("Lista original 1: ", list_1)
print("Lista original 2: ", list_2)
list_1.extend(list_2)
print("Lista agegada: ", list_1)

# 3) insert() --> este metodo nos permite agregar un elemento en una posicion especifica de la lista
money_list = ["dolar", "euro", "yen", "libra", "peso mexicano", "peso colombiano", "peso chileno", "peso argentino", "peso peruano", "peso boliviano"]
print("Lista original: ", money_list)
money_list.insert(2, "peso uruguayo")
print("Lista agregada: ", money_list)

# --------------------------------------------Metodos de replicacion--------------------------------------------
#Este metodo nos permite replicar una lista, estos metodos son los siguientes:

# 1) copy() --> este metodo nos permite replicar una lista
money_list = ["dolar", "euro", "yen", "libra", "peso mexicano", "peso colombiano", "peso chileno", "peso argentino", "peso peruano", "peso boliviano"]
print("Lista original: ", money_list)
list_copy = money_list.copy()
print("Lista replicada: ", list_copy)

# --------------------------------------------Metodos de eliminacion--------------------------------------------
#Este metodo nos permite eliminar elementos de una lista, estos metodos son los siguientes:

# 1) remove() --> este metodo nos permite eliminar un elemento de la lista
list1 = ["Mercurio", "Venus", "Tierra", "Marte", "Jupiter", "Saturno", "Urano", "Neptuno"]
print("Lista original: ", list1)
list1.remove("Tierra")
print("Lista eliminada: ", list1)

# 2) pop() --> este metodo nos permite eliminar un elemento de la lista por posicion
list1.pop(2)
print("Lista eliminada: ", list1)

# 3) clear() --> este metodo nos permite eliminar todos los elementos de la lista
list1.clear()
print("Lista eliminada: ", list1)

# --------------------------------------------Metodos de ordenamiento ------------------------------------------
#Este metodo nos permite ordenar los elementos de una lista, estos metodos son los siguientes:

# 1) sort() --> este metodo nos permite ordenar los elementos de una lista de forma ascendente
numbers_list = [-10, 40, -30, 70, -50, 46, -70, 90, -90, 123]
letters_list = ["a", "d", "z", "b", "c", "f", "g", "h", "i", "j"]

print("Lista original: ", numbers_list)
print("Lista ordenada: ", sorted(numbers_list))
print("Lista original: ", letters_list)
print("Lista ordenada: ", sorted(letters_list))

# 1.1) sort(reverse=True) --> este metodo nos permite ordenar los elementos de una lista de forma descendente

print("Lista ordenada: ", sorted(numbers_list, reverse=True))
print("Lista ordenada: ", sorted(letters_list, reverse=True))

# 2) reverse() --> este metodo nos permite ordenar los elementos de una lista de forma descendente
planets_list = ["Mercurio", "Venus", "Tierra", "Marte", "Jupiter", "Saturno", "Urano", "Neptuno"]
print("Lista original: ", planets_list)
planets_list.reverse()
print("Lista ordenada: ", planets_list)