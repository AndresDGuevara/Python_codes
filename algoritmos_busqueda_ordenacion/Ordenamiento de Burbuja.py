""" Ordenamiento de burbuja: 
 Es un algoritmo que recorre rapidamente una lista que necesita ordenarse. Compara elementos 
 adjacentes y los intercambia si estan en el orden incorrecto. Este procedimiento se repite 
 hasta que no se requiere mas intercambios, lo que indica que la lista se encuentra ordenada

    Aqui tenemos un crecimiento polinominial O(n ** 2)
tambien llamado Bubble Sort
"""
import random
def ordenamiento_de_burbuja(lista):
    n = len(lista) # Lonjitud de la lista (1)

    for i in range(n): # Recorremos la lista n veces
        for j in range(0, n - i - 1): # Busqueda Polinominial, interacion dentro de la interacion

            if lista[j] > lista[j + 1]: # (2)

                   #1          #2               #3        #4
                lista[j], lista[j + 1] = lista [j + 1], lista[j]
                print(lista) # para saber lo que pasa adentro del algoritmo

    return lista

if __name__ == '__main__':

    tamaño_de_lista = int(input('De que tamaño sera la lista: '))
    lista = [random.randint(0, 100) for i in range(tamaño_de_lista)]
    print(lista)

    lista_ordenada = ordenamiento_de_burbuja(lista)
    print(lista_ordenada)

# (1) para ir iterando alrededor de ella, vamos a ir iterando hasta el final 
#     y cada vez uno menos porque ya al final esta garantizado el ordenamiento 
#     de los elementos

# (2) Comparamos los objetos adjacentes, si es menor lo intercambiamos, es decir 
#     intercambiamos variables (swapping)
#   El j + 1 lo estamos pasando a [j] 
#   El #3 lo ponemos en el #1
#   Y el #2 lo ponemos en el #4


# Este algoritmo funciona para lista de pocos elementos, 20 o 49
# Pero en una lista de un millon de elemntos no nos va a funcionar

