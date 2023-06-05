#En python encontramos diferentes tipos de datos en este caso hablasemos de los mas usados:

# 1. String (cadenas de texto)
course_name = "Curso de Python"
#si queremos que se imprima en la consola el texto con comillas debemos usar comillas simples
message = "'Hola mundo'"
#si queremos hacer un salto de linea hay 4 formas de hacelo
# 1.1. Usando \n
message = "Hola mundo \nAdios mundo"
# 1.2. Usando """ """
message = """
Hola mundo
Adios mundo
"""
# 1.3. haciendo lo desde el print
print(message + "\n" + "Adios mundo")
# 1.4. Usando \t realiza un tabulador
message = "Hola mundo \tAdios mundo"
print(message)

# 2. Int (enteros)
number = 3
# 2.1. Podemos tambien imprimir numeros negativos
number = -3
print(number)

# 3. Float (decimales)
float_number = -3.53
float_number = 3.53
print(float_number)
# 3.1 siempre que trabajemos con numeros podemos hacer uso de operadores aritmeticos como:
# 3.1.1. Suma
sum = 3 + 2
print(sum)
# 3.1.2. Resta
rest = 3 - 2
print(rest)
# 3.1.3. Multiplicacion
mult = 3 * 2
print(mult)
# 3.1.4. Division
div = 3 / 2
print(div)
# 3.1.5. Modulo
mod = 3 % 2
print(mod)
# 3.1.6. Exponente
exp = 3 ** 2
print(exp)
# 3.1.7. Division entera
div_int = 3 // 2
print(div_int)

# 4. Bool (verdadero o falso)
boolean = True
false_boolean = False
print(boolean)
print(false_boolean)
