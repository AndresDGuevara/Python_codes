""" Ordenamiento por insercion (Inserction Sort) que tambien sigue el algoritmo 
O(n ** 2) o algoritmo polonominial
tambien llamado Insertion Sort
"""

import random

def ordenamiento_por_insercion(lista):

  for i in range(1, len(lista)):
    valor_actual = lista[i]
    posicion_actual = i
    #print(lista)
    while posicion_actual > 0 and lista[posicion_actual - 1] > valor_actual:
      lista[posicion_actual] = lista[posicion_actual - 1]
      posicion_actual -= 1

    lista[posicion_actual] = valor_actual
  return lista

if __name__ == '__main__': 
  tamaño_de_lista = int(input('De que tamaño sera la lista :')) 
    
  lista = [random.randint(0, 100) for i in range(tamaño_de_lista)]
  print(lista)

  lista_ordenada = ordenamiento_por_insercion(lista)
  print(lista_ordenada)

""" 
Una lista es dividida entre una sublista ordenada y otra sublista desordenada.
Al principio, la sublista ordenada contiene un solo elemento, por lo que por
definición se encuentra ordenada.

A continuación se evalua el primer elemento dentro la sublista desordenada para
que podamos insertarlo en el lugar correcto dentro de la lista ordenada.

La inserción se realiza al mover todos los elementos mayores al elemento que
se está evaluando un lugar a la derecha.

Continua el proceso hasta que la sublista desordenada quede vacia y, por lo
tanto, la lista se encontrará ordenada.
"""