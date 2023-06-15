# Accesibilidad de los elementos de una tupla

tuple1 = ("lujuria", "gula", "avaricia", "pereza", "ira", "envidia", "soberbia")

# De esta forma podrmos trabajar 3 formas de acceder a los elementos de una tupla

#1) Accesibilidad por posición (modo por defecto)

print(tuple1[0]) # lujuria
print(tuple1[5]) # envidia

#2) Accesibilidad por índice negativo (modo inverso)

print(tuple1[-1]) # soberbia
print(tuple1[-3]) # ira

#3) Accesibilidad por rango (modo slice)

print(tuple1[0:3]) # ('lujuria', 'gula', 'avaricia')
print(tuple1[3:6]) # ('pereza', 'ira', 'envidia')

# Longitud de una tupla

tuple3 = ("manzana", "pera", "naranja", "plátano", "sandía", "melón", "uva", "fresa", "cereza", "kiwi")

print(len(tuple3)) # 10

# Union de tuplas

# primera forma
tuple4 = ("j", "m", "a", "n", "u", "e", "l")
tuple5 = (1, 2, 3, 4, 5, 6, 7)

print(tuple4 + tuple5) # ('j', 'm', 'a', 'n', 'u', 'e', 'l', 1, 2, 3, 4, 5, 6, 7)

# segunda forma

tuple6 = tuple4 + tuple5
print(tuple6) # ('j', 'm', 'a', 'n', 'u', 'e', 'l', 1, 2, 3, 4, 5, 6, 7)

# Conversion de tuplas a listas y viceversa

#En este caso tenemos una tupla y una lista una tupla de ciudades y una lista de balnearios

cieties = ("lima", "bogota", "santiago", "quito", "caracas", "buenos aires", "brasilia", "montevideo", "asuncion", "la paz")

print(cieties) # ('lima', 'bogota', 'santiago', 'quito', 'caracas', 'buenos aires', 'brasilia', 'montevideo', 'asuncion', 'la paz')
print(type(cieties)) # <class 'tuple'>

spas = ["mancora", "cartagena", "valparaiso", "baños", "los roques", "mar del plata", "florianopolis", "punta del este", "encarnacion", "santa cruz"]
print(spas) # ['mancora', 'cartagena', 'valparaiso', 'baños', 'los roques', 'mar del plata', 'florianopolis', 'punta del este', 'encarnacion', 'santa cruz']
print(type(spas)) # <class 'list'>

# Conversion de tupla a lista

cieties = list(cieties)
print(cieties) # ['lima', 'bogota', 'santiago', 'quito', 'caracas', 'buenos aires', 'brasilia', 'montevideo', 'asuncion', 'la paz']
print(type(cieties)) # <class 'list'>

# Conversion de lista a tupla

spas = tuple(spas)
print(spas) # ('mancora', 'cartagena', 'valparaiso', 'baños', 'los roques', 'mar del plata', 'florianopolis', 'punta del este', 'encarnacion', 'santa cruz')
print(type(spas)) # <class 'tuple'>