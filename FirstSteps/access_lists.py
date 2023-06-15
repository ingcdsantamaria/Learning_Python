# 1) Accesibilidad de listas
list1 = ["manzana", "platano", "naranja", "pera", "fresa", "melon", "sandia", "mango", "papaya", "piña"]

# formas de accesibilidad por posicion
print("Accesibilidad por posicion, posicion 0: ", list1[0])
print("Accesibilidad por posicion, posicion 5: ", list1[5])

# Formas de accesibilidad por posicion negativa
print("Accesibilidad por posicion negativa, posicion -1: ", list1[-1])
print("Accesibilidad por posicion negativa, posicion -4: ", list1[-4])

# Formas de accesibilidad por rango
print("Accesibilidad por rango, posicion 0 a 5: ", list1[0:5])
print("Accesibilidad por rango, posicion 5 a 10: ", list1[5:10])

# 2) En esta parte veremos la longitud de las listas
list1 = ["manzana", "platano", "naranja", "pera", "fresa", "melon", "sandia", "mango", "papaya", "piña"]
print("Longitud de la lista: ", len(list1))

# 3) #En este apartado hablaremos de la union de listas, para unir listas
list1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Primera forma de unir listas
print("Primera forma de unir listas: ", list1 + list2)

# Segunda forma de unir listas
list3 = list1 + list2
print("Segunda forma de unir listas: ", list3)
