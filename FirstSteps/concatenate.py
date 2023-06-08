#En esta seccion veremos las formas de concatenar strings en python, ejemplo:
# 1. Concatenar con +
course_name = "Curso de Python"
message = "Hola, bienvenido al " + course_name
print(message)

# 2. Concatenar con format
course_name = "Curso de Python"
message = "Hola, bienvenido al {}".format(course_name)#en este caso se usa {} para indicar que ahi va el valor de la variable course_name, y con format() le decimos cual es el valor que va a ir ahi en los {}
print(message)

#tambien podemos concatenar mas de una variable, ejemplo:
course_name = "Curso de Python"
course_name2 = "Curso de Java"
message = "Hola, bienvenido al {} y al {}".format(course_name, course_name2)#en este caso se usa {} para indicar que ahi va el valor de la variable course_name, y con format() le decimos cual es el valor que va a ir ahi en los {}
print(message)

# 3. Concatenar con f
course_name = "Curso de Python"
message = f"Hola, bienvenido al {course_name}"#en este caso se usa {} para indicar que ahi va el valor de la variable course_name, y con f le decimos que es una variable
print(message)

#4. Concatenar con , (no es muy usado)
course_name = "Curso de Python"
message = "Hola, bienvenido al "
print(message, course_name)
#Nota: si intentamos concatenar dentro de una variable nos imprimira entre () y separado por comas.

