
#Los operadores logicos estan conformados por: and, or, not
"""
acontinuacion veras 3 tablas de verdad, la primera es la tabla de verdad del operador and, la segunda es la tabla de verdad del operador or y la tercera es la tabla de verdad del operador not

donde a y b son variables y pueden tomar los valores de 0 o 1 (False o True)
_____________________________________________________________________________________
||  a  ||  b  ||  a and b  ||  a or b  ||  not a  ||  not b  ||  not a and not b  ||
||  0  ||  0  ||     0     ||     0    ||    1    ||    1    ||         1         ||
||  0  ||  1  ||     0     ||     1    ||    1    ||    0    ||         0         ||
||  1  ||  0  ||     0     ||     1    ||    0    ||    1    ||         0         ||
||  1  ||  1  ||     1     ||     1    ||    0    ||    0    ||         0         ||
_____________________________________________________________________________________

"""

# Ejemplo:
num1 = 5
num2 = 15
num3 = 10
num4 = 20
print("El numero 1 es menor que el numero 2 y el numero 3 es menor que el numero 4: ", num1 < num2 and num3 < num4)
print("El numero 1 es menor que el numero 2 o el numero 3 es menor que el numero 4: ", num1 < num2 or num3 < num4)
print("El numero 1 es menor que el numero 2 y el numero 3 es mayor que el numero 4: ", num1 < num2 and num3 > num4)
print("El numero 1 es menor que el numero 2 o el numero 3 es mayor que el numero 4: ", num1 < num2 or num3 > num4)
#ahora con el operador not
print("El numero 1 es menor que el numero 2 y el numero 3 es menor que el numero 4: ", not(num1 < num2 and num3 < num4))