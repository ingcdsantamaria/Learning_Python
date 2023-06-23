# En este archivo hablaremos del condicional if, el condicional if es un condicional que nos permite ejecutar un bloque de codigo si se cumple una condicion.
#Ejemplo:
# Ingrese su edad en el teclado y si es mayor de edad le mostrara un mensaje si no es mayor de edad le mostrara otro mensaje

age = int(input("Ingrese su edad: "))

if age >= 18:
    print("Usted es mayor de edad")

# Ahora hablaremos del condicional ELIF, el condicional elif es un condicional que nos permite ejecutar un bloque de codigo si se cumple una condicion y si no se cumple la condicion anterior, este condicional se puede usar cuantas veces se desee, pero siempre debe ir despues de un condicional if o de un condicional elif
# Ejemplo:

# Ingrese dos numeros por teclado, este calculara su division, escribiendo si la divicion es exacta o no
numDvd = int(input("Ingrese el dividendo: "))
numDvs = int(input("Ingrese el divisor: "))

if numDvs == 0:
    print("No se puede dividir entre 0")
elif numDvd % numDvs == 0:
    print("La division es exacta")# Una division es exacta cuando el residuo es 0
else:# El else se utiliza para ejecutar un bloque de codigo si no se cumple ninguna de las condiciones anteriores
    print("La division no es exacta")

# Otro ejemplo seria el siguiente:
# Ingrese por teclado el nombre de la moneda de un pais y valide si existe en la lista de monedas
coinDenomination = input("Ingrese el nombre de la moneda: ")
listCoins = ["Peso", "Dolar", "Euro", "Yen", "Libra"]

# Ahora convertiremos la primer letra de la moneda que se ingrese en mayuscula, ya que como en la lista la primer letra de cada moneda esta en mayuscula, si no se hace esto el programa no encontrara la moneda o la otra opcion es dejar la lista en minuscula o en mayuscula
coinDenomination = coinDenomination.capitalize()

if coinDenomination in listCoins:
    print("La moneda existe")
else:
    print("La moneda no existe")