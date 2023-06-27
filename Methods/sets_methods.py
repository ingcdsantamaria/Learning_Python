# En este archivo veremos los tipos de metodos para los conjuntos (set), estos se van a clasificar de la siguiente manera:

# 1) Metodos de agregacion: Estos metodos nos permiten agregar elementos a un conjunto set y los metodos son los siguientes:

# * add(): Este metodo nos permite agregar un elemento al conjunto set

setFelines = set(["Tiger", "Lion", "Jaguar", "Leopard", "Cheetah", "Puma"])
print(setFelines)

setFelines.add("Panther") # Lo que estamos haciendo es agregar el elemento "Panther" al conjunto setFelines
print(setFelines)

# * update(): Este metodo nos permite agregar varios elementos al conjunto o cualquier iterable y juntarlos con el conjunto actual

setConuntry = set(["Peru", "Colombia", "Argentina", "Chile", "Ecuador"])
print(setConuntry)

set_asia = set(["China", "India", "Japan", "Korea", "Thailand"])
print(set_asia)

setConuntry.update(set_asia) # Lo que estamos haciendo es agregar los elementos del conjunto set_asia al conjunto setConuntry

print(setConuntry)

# * union(): Este metodo nos permite unir dos conjuntos set

setCompanies = set(["GOOGLE", "MICROSOFT", "APPLE", "AMAZON", "FACEBOOK"])
print(setCompanies)

setHardware = set(["DELL", "HP", "LENOVO", "ASUS", "ACER"])
print(setHardware)

set_in = setCompanies.union(setHardware) # Lo que estamos haciendo es unir los conjuntos setCompanies y setHardware y guardarlo en la variable set_in
print(set_in)

# 2) Metodos de replicacion: Estos metodos nos permiten replicar un conjunto set y los metodos son los siguientes:

# * copy(): Este metodo nos permite copiar un conjunto set

setMoney = set(["PEN", "USD", "EUR", "JPY", "GBP"])
print(setMoney)

copy_setMoney = setMoney.copy() # Lo que estamos haciendo es copiar el conjunto setMoney y guardarlo en la variable copy_setMoney
print(copy_setMoney)

# 3) Metodos de eliminacion: Estos metodos nos permiten eliminar elementos de un conjunto set y los metodos son los siguientes:

# * remove(): Este metodo nos permite eliminar un elemento de un conjunto set

setPlanets = set(["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"])
print(setPlanets)

setPlanets.remove("Mercury") # Lo que estamos haciendo es eliminar el elemento "Mercury" del conjunto setPlanets
print(setPlanets)

# * discard(): Este metodo nos permite eliminar un elemento de un conjunto set

setPlanets.discard("Venus") # Lo que estamos haciendo es eliminar el elemento "Venus" del conjunto setPlanets
print(setPlanets)
#La diferencia en entre remove y discard es que remove si el elemento no existe en el conjunto set nos devolvera un error, en cambio discard si el elemento no existe en el conjunto set no nos devolvera ningun error ejemplo:

setPlanets.discard("Pluto") # Lo que estamos haciendo es eliminar el elemento "Pluto" del conjunto setPlanets, pero como el elemento "Pluto" no existe en el conjunto setPlanets no nos devolvera ningun error

# * pop(): Este metodo nos permite eliminar el ultimo elemento de un conjunto set, ten encuenta la posicion cuando se ejecuata ya que es aleatorio

setPlanets.pop() # Lo que estamos haciendo es eliminar el ultimo elemento del conjunto setPlanets
print(setPlanets)

# * clear(): Este metodo nos permite eliminar todos los elementos de un conjunto set

setPlanets.clear() # Lo que estamos haciendo es eliminar todos los elementos del conjunto setPlanets
print(setPlanets)

