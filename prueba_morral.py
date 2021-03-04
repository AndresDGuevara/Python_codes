""" Algoritmo para resover problemas de constrain
"""
def morral(tamano_morral, pesos, valores, n):

# caso base
    if n == 0 or tamano_morral == 0: # ya no nos queda mas elememntos o el morral se lleno
        return 0

# otro caso base 
# si el peso del elemnto n es mayor que el morral vamos al siguiente elemento
    if pesos[n - 1] > tamano_morral:
        return morral(tamano_morral, pesos, valores, n - 1)

# parte importante de la funcion
# max = escoger cual es el valor maximo entre dos valores posibles
   #  sumatoria de valores, llamos al morral haciendolo mas pequeñp
   # restando el peso. n -1 es pasemos al siguiente elemento
    return max(valores[n - 1] + morral(tamano_morral - pesos[n - 1], pesos, valores, n - 1),
                morral(tamano_morral, pesos, valores, n - 1))


if __name__ == '__main__':
    valores = [60, 100, 120]
    pesos = [10, 20, 30]
    tamano_morral = 50
    n = len(valores)

    resultado = morral(tamano_morral, pesos, valores, n)
    print(resultado)
