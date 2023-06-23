# El ciclo while se utiliza para repetir un bloque de codigo mientras se cumpla una condicion, es decir, mientras la condicion sea verdadera se ejecutara el bloque de codigo, cuando la condicion sea falsa se terminara el ciclo, el ciclo while se puede usar con las sentencias break y continue


#*NOTA: Es importante ya tener claro los operadores relacionales

n = 10
# Incremento
while n < 30:
    print(n)
    n += 1# <-- Esto es igual o decir n = n + 1
print("SE FINALIZO EL CICLO")

# Decremento
y = 5

while y >= -5:
    print(y)
    y -= 1
print("SE FINALIZO EL CICLO ")

# Diferente

wordKey = input("Ingrese la palabra clave para salir del ciclo: \n")

while wordKey != "Salir":
    wordKey = input("Ingrese la palabra clave para salir del ciclo: \n")
    print(wordKey)
print("La palabra es correcta a logrado salir")

#----------------------------------------------------------------------------------

# Ahora hablaremos de la sentencia break y continue con el ciclo while

n = 7
while n < 20:
    print(n)
    if n == 15:
        break
    n += 1
print("SE FINALIZO EL CICLO")

# Ahora hablaremos de la sentencia continue
y = 25

while y > 0:
    y -= 1
    if y == 20:
        continue
    print(y)