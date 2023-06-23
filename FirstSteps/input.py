# Este archivo hablaremos de inputs Un input es una funcion que nos permite ingresar datos desde el teclado y encontramos 2 formas de hacerlo strings y numeros

# Para ingresar un string usamos la funcion input() y dentro de los parentesis podemos poner un mensaje que queramos que aparezca en la consola
name = input("Ingrese su nombre: ")
print("Hola " + name)

# Para ingresar un numero usamos la funcion input() y dentro de los parentesis podemos poner un mensaje que queramos que aparezca en la consola
age = int(input("Ingrese su edad: "))
print("Su edad es: ", age)

weight = float(input("Ingrese su peso: "))
print("Su peso es: ", weight)

# Si se desea concatenar con + dese convertir el input a string ejemplo
print("Su edad es: " + str(age))