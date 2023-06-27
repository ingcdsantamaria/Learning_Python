# Ahora hablaremos sobre la accesibilidad de los elementos de un conjunto set, para ello crearemos un conjunto set con datos de diferentes tipos

# 1) Accesibilidad set (conjuntos)

setBank = set(["BCP", "BBVA", "Interbank", "Pichincha", "Scotiabank"])
print(type(setBank)) # Lo que estamos haciendo es preguntar el tipo de dato que es setBank, nos devolvera que es un conjunto set

# 2) Accesibilidad por valor especifico aplicando el operador in

print("BCP" in setBank) # Lo que estamos haciendo es preguntar si el valor "BCP" esta dentro del conjunto setBank, si esta dentro del conjunto setBank nos devolvera True, de lo contrario nos devolvera False
print("Azteca" in setBank)

# 3) Accesibilidad por bucle FOR

for i in setBank: # Lo que estamos haciendo es recorrer el conjunto setBank, y por cada elemento que tenga el conjunto setBank nos imprimira en consola el elemento
    print(i)

#--------------------------------------------------------------------------------------
# En esta seccion veremos la longitud de un conjunto set, para ello crearemos un conjunto set con datos de diferentes tipos

listBank = ["BCP", "BBVA", "Interbank", "Pichincha", "Scotiabank", "Santander"]
setBank = set(listBank) # Lo que estamos haciendo es convertir la lista listBank en un conjunto setBank y guardarlo en la variable setBank

print(len(setBank)) # Lo que estamos haciendo es preguntar la longitud del conjunto setBank, nos devolvera la cantidad de elementos que tiene el conjunto setBank

#--------------------------------------------------------------------------------------