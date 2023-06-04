import random
import math

# Función para determinar si un número es primo
def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

# Función para generar números primos aleatorios
def generar_primos():
    p = random.randint(100, 500)
    while not es_primo(p):
        p += 1
    q = random.randint(100, 500)
    while not es_primo(q) or p == q:
        q += 1
    return p, q

# Función para calcular la clave pública y privada
def generar_claves(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 3
    while math.gcd(e, phi) != 1:
        e += 2
    d = pow(e, -1, phi)
    return (n, e), (n, d)

# Función para cifrar un mensaje
def cifrar(msg, clave_publica):
    n, e = clave_publica
    cifrado = [pow(ord(c), e, n) for c in msg]
    return cifrado

# Función para descifrar un mensaje
def descifrar(cifrado, clave_privada):
    n, d = clave_privada
    descifrado = [chr(pow(c, d, n)) for c in cifrado]
    return ''.join(descifrado)

# Función para pedir al usuario un mensaje
def pedir_mensaje():
    return input("Introduce el mensaje que quieres cifrar: ")

# Función principal del programa
def main():
    p, q = generar_primos()
    clave_publica, clave_privada = generar_claves(p, q)
    mensaje = pedir_mensaje()
    mensaje_cifrado = cifrar(mensaje, clave_publica)
    mensaje_descifrado = descifrar(mensaje_cifrado, clave_privada)
    print("Mensaje original: ", mensaje)
    print("Mensaje cifrado: ", mensaje_cifrado)
    print("Mensaje descifrado: ", mensaje_descifrado)

if __name__ == '__main__':
    main()