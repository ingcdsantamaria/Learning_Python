#python maneja la siguiente estuctura de datos
#ejemplo <nombre de la variable> = <valor de la variable>
curso = "Curso de Python"
#una variable puede modificar su valor en cualquier momento
curso = "Curso de Python 3"
#para imprimir el valor de una variable se usa la funcion print
print(curso)
#nota: siempre que se creen nuevas variables intenta que los nombres sean bien descriptivos, claros y concisos por ejemplo:
titulo_curso = "Curso de Python 3"
#siempre que nosotros utilicemos 2 palabras para nombrar una variable se recomienda utilizar el formato snake_case o la nomenclatura camelCase para poner la segunda letra en mayuscula ejemplo:
tituloCurso = "Curso de Python 3"
#hay ciertas palabras que no podemos utilizar a estas se les denomina palabras reservadas son palabras que ya estan reservadas por el lenguaje de programacion para realizar ciertas acciones en particular
#listado de palabras reservadas es el siguiente:
#False, None, True, and, as, assert, break, class, continue, def, del, elif, else, except, finally, for, from, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield
# es importante resaltar el aprender ingles, esto porque la mayoria de los lenguajes de programacion estan en ingles y sus variables por buenas practicas se deben de nombrar en ingles, desde aqui empezaremos a utilizar el ingles para nombrar nuestras variables ejemplo:
course_name = "Curso de Python 3"
print(course_name)

#jamas pongas al nombre de varioables numeros al inicio ejemplo:
# 1curso = "Curso de Python 3"
# o guiones comas o simbolos raros ejemplo:
# curso-1 = "Curso de Python 3"
# esto por que python no lo permite y nos dara un error por sintaxis

#asignar variables multiples
#en python podemos asignar multiples variables en una sola linea de codigo ejemplo:
x, book = 100, "I Robot"
print(x)
print(book)
#podemos asignar el mismo valor a multiples variables ejemplo:
x = book = 100
print(x)
print(book)
