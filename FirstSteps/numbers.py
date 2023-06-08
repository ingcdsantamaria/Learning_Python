#cabe destacar que aunque casi no se utiliza en python tambien existen los numeros complejos
complex_number = 3 + 2j
print(complex_number)
print(type(complex_number))

#tambien hablaremos de la conversion de numeros la primera sera de int a float
number = 3
float_number = float(number)
print(float_number)
print(type(float_number))

#la segunda sera de float a int
float_number = 3.5
number = int(float_number)
print(number)
print(type(number))

#la tercera sera de int a string
number = 3
string_number = str(number)
print(string_number)
print(type(string_number))

#la cuarta sera de string a int
string_number = "3"
number = int(string_number)
print(number)
print(type(number))

#la quinta sera de string a float
string_number = "3.5"
float_number = float(string_number)
print(float_number)
print(type(float_number))

#la sexta sera de float a string
float_number = 3.5
string_number = str(float_number)
print(string_number)
print(type(string_number))

#la septima sera de complex a string
complex_number = 3 + 2j
string_number = str(complex_number)
print(string_number)
print(type(string_number))



#la onceava sera de complex a int
"""complex_number = 3 + 2j
number = int(complex_number.real)
print(number)
print(type(number))
"""

# nos lanzara un error ya que no podemos convertir un numero complejo a int ya que este tiene una parte imaginaria y una real y no podemos convertirlo a int

#ahora hablaremos de los redondeos de numeros esto se hace con la funcion round()
#si el numero es menor a 0.5 se redondea hacia abajo
#si el numero es mayor a 0.5 se redondea hacia arriba
#si el numero es igual a 0.5 se redondea hacia arriba
number = 3.5
print(round(number))
number = 3.4
print(round(number))
number = 3.6
print(round(number))
#si queremos redondear a un numero especifico debemos pasarle un segundo parametro a la funcion round(), este parametro sera el numero de decimales que queremos que tenga el numero.
number = 3.141592653589793
print(round(number, 2))


