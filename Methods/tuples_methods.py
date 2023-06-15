# Metodos de las tuplas, contamos con solo dos metodos metodos count() y index()

#1) Primer metodo count() --> cuenta la cantidad de veces que se repite un elemento en una tupla

tuple1 = ("Francia", "Colombia", "Peru", "Argentina", "Colombia", "Peru", "Colombia", "Peru")
print(tuple1.count("Colombia")) # 3
print(tuple1.count("Peru")) # 3
print(tuple1.count("Francia")) # 1

#2) Segundo metodo index() --> busca en la tupla el elemento que le pasemos por parametro y nos devuelve el indice de la primera coincidencia

tuple2 = ("Sol", "Luna", "Marte", "Venus", "Tierra", "Mercurio", "Jupiter", "Saturno", "Urano", "Neptuno", "Pluton")

print(tuple2.index("Tierra")) # 4
print(tuple2.index("Marte")) # 2
print(tuple2.index("Pluton")) # 10
