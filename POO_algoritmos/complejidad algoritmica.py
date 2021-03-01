import time

def factorial(n):
    respuesta = 1

    while n > 1:
        respuesta *= n
        n -= 1

    return respuesta


def factorial_r(n):
    if n == 1:
        return 1

    return n * factorial(n - 1)


if __name__ == '__main__':
    n = 100000

    comienzo = time.time()
    factorial(n) # imprimir cual es el factorial de n pero llevaria mucho y nos distraeria de lo que es importante que es el tiempo
    final = time.time()
    print(final - comienzo)  #medimos cuanto tiempo se tarda

    comienzo = time.time()
    factorial_r(n)  #factorial recursivo
    final = time.time()
    print(final - comienzo)

    #implementacion recursiva
#implementacion iterativa
#esta medida de tiempo no nos va a servir porque depende del hardware de la computadora, 
# de los programas que se tengan abiertos etc.