#METODOS STRINGS

# Los metodos que podemos encontrar solo para el tipo de dato string son los siguientes:
"""
len(): Retorna la longitud de la cadena de caracteres.
lower(): Convierte la cadena de caracteres a minúsculas.
upper(): Convierte la cadena de caracteres a mayúsculas.
capitalize(): Convierte la primera letra de la cadena de caracteres a mayúscula y el resto a minúsculas.
title(): Convierte cada palabra en la cadena de caracteres a mayúscula.
count(substring): Cuenta el número de ocurrencias de una subcadena en la cadena de caracteres.
find(substring): Retorna la posición de la primera ocurrencia de una subcadena en la cadena de caracteres.
replace(old, new): Reemplaza todas las apariciones de una subcadena por otra en la cadena de caracteres.
split(delimiter): Divide la cadena de caracteres en una lista de subcadenas utilizando un delimitador.
strip(): Elimina los espacios en blanco al inicio y final de la cadena de caracteres.
startswith(prefix): Verifica si la cadena de caracteres comienza con una determinada subcadena.
endswith(suffix): Verifica si la cadena de caracteres termina con una determinada subcadena.
isalpha(): Verifica si la cadena de caracteres contiene solo letras.
isdigit(): Verifica si la cadena de caracteres contiene solo dígitos numéricos.
Entre otros.
"""
# 1) replace() --> Reemplaza una cadena por otra
# ejemplo:
sentence = "The dog is named Sammy, and the cat is Oscar"
print(sentence)
sentence = sentence.replace("dog", "hamster")
print(sentence)
# esto tambien se puede realizar en un parrafo con todas las palabras que se deseen reemplazar
# ejemplo:
sentence = "Pablito clavo un clavito, en la calva de un calvito, en la calva de un calvito, Pablito clavo un clavito"
print(sentence)
sentence = sentence.replace("Pablito", "Pedrito")
print(sentence)

# 2) count() --> Cuenta cuantas veces aparece una cadena en otra
# ejemplo:
sentence = "The dog is named Sammy, and the cat is Oscar"
print(sentence)
print(sentence.count("is"))
# esto tambien se puede realizar en un parrafo con todas las palabras que se deseen contar
# ejemplo:
sentence = "En el vasto y frondoso bosque, donde los árboles se alzaban majestuosos y la luz del sol se filtraba entre las hojas, vivía una comunidad de animales. Los animales del bosque eran diversos en especies y tamaños. Había conejos escurridizos, ardillas ágiles, zorros astutos y aves de colores brillantes. Sin embargo, entre todos ellos, había una criatura especial: el pequeño y curioso ratón. El ratón, con su pelaje suave y ojos brillantes, exploraba incansablemente cada rincón del bosque en busca de aventuras. En su búsqueda constante, el ratón descubría tesoros escondidos y compartía su hallazgo con entusiasmo. Los demás animales, maravillados por las hazañas del ratón, seguían con atención cada uno de sus pasos. El ratón se había convertido en una figura admirada y respetada por todos. Su coraje, inteligencia y generosidad eran su sello distintivo. En el bosque, el ratón era más que un simple roedor; era una inspiración para los demás."
print(sentence)
print(sentence.count("ratón"))

# 3) upper() --> Convierte una cadena a mayusculas
# ejemplo:
sentence = "The dog is named Sammy, and the cat is Oscar"
print(sentence)
print(sentence.upper())

# 4) lower() --> Convierte una cadena a minusculas
# ejemplo:
sentence = "THE DOG IS NAMED SAMMY, AND THE CAT IS OSCAR"
print(sentence)
print(sentence.lower())
# no es necesario que todo el texto este en mayusculas o minusculas, se puede mezclar, ejemplo:
sentence = "The dog is named Sammy, and the cat is Oscar"
print(sentence)
print(sentence.lower())

# 5) capitalize() --> Convierte la primera letra de una cadena a mayuscula
# ejemplo:
sentence = "THE DOG is named Sammy, and the cat is Oscar"
print(sentence)
print(sentence.capitalize())

# 6) title() --> Convierte la primera letra de cada palabra de una cadena a mayuscula
# ejemplo:
text = "Juan Carlos, renueva el televisor de su sala o adquiere la laptop que necesitas compranto en nuestra tienda"
print(text)
print(text.title())

# 7) strip() --> Elimina los espacios en blanco al inicio y al final de una cadena
# ejemplo:
text = "    Juan Carlos, renueva el televisor de su sala o adquiere la laptop que necesitas compranto en nuestra tienda    "
print(text)
print(text.strip())

# 8) lstrip() --> Elimina los espacios en blanco al inicio de una cadena
# ejemplo:
text = "    Juan Carlos, renueva el televisor de su sala o adquiere la laptop que necesitas compranto en nuestra tienda    "
print(text)
print(text.lstrip())

# 9) format() --> Permite formatear una cadena
# re encuentran 3 formas de formatear una cadena:
# 9.1) Orden predeterminado
# ejemplo:
name_1 = "Juan"
name_2 = "Carlos"
name_3 = "Pedro"

order_predetermined = "{} obtuvo el primer lugar, {} el segundo lugar y {} el tercer lugar"
print(order_predetermined.format(name_1, name_2, name_3))
# 9.2) Orden usando el argumento de posicionamiento
# ejemplo:
name_1 = "Juan"
name_2 = "Carlos"
name_3 = "Pedro"

order_positioning = "{1} obtuvo el primer lugar, {2} el segundo lugar y {0} el tercer lugar"
print(order_positioning.format(name_1, name_2, name_3))
# 9.3) Orden usando el argumento de palabras clave
# ejemplo:
name_1 = "Juan"
name_2 = "Carlos"
name_3 = "Pedro"

order_keyword = "{c} obtuvo el primer lugar, {p} el segundo lugar y {j} el tercer lugar"
print(order_keyword.format(j = "Juan", c = "Carlos", p = "Pedro"))

# 10) split() --> Divide una cadena en subcadenas
# ejemplo:
sentence = "The dog is named Sammy, and the cat is Oscar"
print(sentence)
print(sentence.split())
# ejemplo:
sentence = "The dog is named Sammy, and the cat is Oscar"
print(sentence)
print(sentence.split(","))

# 11) len() --> Devuelve la longitud de una cadena
# ejemplo:
sentence = "The dog is named Sammy, and the cat is Oscar"
print(sentence)
print(len(sentence))

# 12) find() --> Busca una subcadena en una cadena y devuelve la posición de la primera coincidencia
# ejemplo:
sentence = "The dog is named Sammy, and the cat is Oscar"
print(sentence)
print(sentence.find("cat"))

# 13) startswith() --> Verifica si la cadena de caracteres comienza con una determinada subcadena
# ejemplo:
sentence = "The dog is named Sammy, and the cat is Oscar"
print(sentence)
print(sentence.startswith("The"))
print(sentence.startswith("the"))

# 14) endswith() --> Verifica si la cadena de caracteres termina con una determinada subcadena
# ejemplo:
sentence = "The dog is named Sammy, and the cat is Oscar"
print(sentence)
print(sentence.endswith("Oscar"))
print(sentence.endswith("Sammy"))

# 15) isdigit() --> Verifica si la cadena de caracteres contiene solo digitos|
# ejemplo:
sentence = "The dog is named Sammy, and the cat is Oscar"
print(sentence)
print(sentence.isdigit())
sentence = "123456789"
print(sentence)
print(sentence.isdigit())

# 16) isalpha() --> Verifica si la cadena de caracteres contiene solo letras
# ejemplo:
sentence = "The dog is named Sammy, and the cat is Oscar"
print(sentence)
print(sentence.isalpha())
sentence = "The dog is named Sammy and the cat is Oscar"
print(sentence)
print(sentence.isalpha())

# 17) isalnum() --> Verifica si la cadena de caracteres contiene solo letras y digitos
# ejemplo:
sentence = "The dog is named Sammy, and the cat is Oscar"
print(sentence)
print(sentence.isalnum())



