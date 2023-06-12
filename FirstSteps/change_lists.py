#En este archivo veremos como cambiar elementos de una lista

# 1) Primera forma de cambiar elementos de una lista cambiando el valor de la posicion
list1 = [10, -15, "20", "129.7", -40]
print("Lista original: ", list1)
list1[4] = False
print("Lista cambiada: ", list1)

# 2) Segunda forma de cambiar elementos de una lista cambio entre rango
list2 = ["lima", 2022, "peru", 2021, "colombia", 2020, "Bogota", 2019, "chile", 2018]
print("Lista original: ", list2)
list2[1:4] = ["mexico", 2017, "argentina"]
print("Lista cambiada: ", list2)

