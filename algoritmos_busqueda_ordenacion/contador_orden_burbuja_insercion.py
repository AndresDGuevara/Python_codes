import random
#import time

def ordenamiento_de_burbuja(lista, iteracion_burbuja = 0):
    n = len(lista) # Lonjitud de la lista (1)

    for i in range(n): # Recorremos la lista n veces
        
        for j in range(0, n - i - 1): # Busqueda Polinominial, interacion dentro de la interacion

            if lista[j] > lista[j + 1]: # (2)
                           
                   #1          #2               #3        #4
                lista[j], lista[j + 1] = lista [j + 1], lista[j]
                print(lista) # para saber lo que pasa adentro del algoritmo
                iteracion_burbuja += 1

    return lista, iteracion_burbuja

def ordenamiento_por_insercion(lista, iteracion_insercion = 0):

    for i in range(1, len(lista)):
                
        valor_actual = lista[i]
        posicion_actual = i
        print(lista)

        while posicion_actual > 0 and lista[posicion_actual - 1] > valor_actual:
            lista[posicion_actual] = lista[posicion_actual - 1]
            posicion_actual -= 1
            iteracion_insercion += 1

        lista[posicion_actual] = valor_actual
    return lista, iteracion_insercion


if __name__ == '__main__':

    tamaño_de_lista = int(input('De que tamaño sera la lista: '))
    
    print("\n---Ordenamiento de Burbuja---")
    lista1 = [random.randint(0, 100) for i in range(tamaño_de_lista)]
    print(lista1)
 
    (lista_ordenada, iteracion_burbuja) = ordenamiento_de_burbuja(lista1)
    print(lista_ordenada)
    print(f'Las Iteraciones fueron: {iteracion_burbuja}')

    print("\n---Ordenamiento por Insercion---")
    lista2 = [random.randint(0, 100) for i in range(tamaño_de_lista)]
    print(lista2)

    (lista_ordenada, iteracion_insercion) = ordenamiento_por_insercion(lista2)
    print(lista_ordenada)
    print(f'Las Iteraciones fueron: {iteracion_insercion}')