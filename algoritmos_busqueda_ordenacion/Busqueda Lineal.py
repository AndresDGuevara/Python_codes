""" Algoritmo de busqueda que nos permite encontrar un elemento que esta o no esta dentro de una estructura de datos.
    La complegidad algoritmica de este codigo es O(n) 
    Algoritmo lineal
    si tu lista no esta ordenada y la vas a utilizar una sola vez, usar este algoritmo 
"""
import random # este modulo nos premite generar numeros aleatorios

def busqueda_lineal(lista, objetivo):
    match = False
    for elemento in lista: # O(n)
        if elemento == objetivo:
            match = True
            break # 1-
    return match

if __name__ == '__main__': # 2-

    tamaño_de_la_lista = int(input('De que tamaño sera la lista: '))
    objetivo = int(input('¿Que numero quieres encontrar?: '))

    lista = [random.randint(0, 100) for i in range(tamaño_de_la_lista)] # 3-

    encontrado = busqueda_lineal(lista, objetivo) #le pasamos la lista que generamos y le pasamos el objetivo que nos pidio el usuario

    print(lista) # imprimimos la lista para saber que esta sucediendo con los numeros aleatorios

    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista') # 4-

# 1- Este break es para cuando estamos en el mejor caso, en promedio nos estariamos tardando menos.
#    pero siempre debemos pensar en el peor caso y este break no nos serviria 

# 2- aqui queremos que el modulo de busqueda_lineal se pueda inportar en otro programa 
#    pero a la vez queremos ejecutarlo de manera directa. con name == main

# 3- Aqui generamos nuestra lista del tamaño_de_lista llena de numeros aleatorios de 0 a 100

# 4- generamos concatenacion para decirle al usuario si se encontro o no
#    tambien generamos algo nuevo, (operadores ternarios) que es generar un if y un else en una misma linea de codigo
#    en operadores ternarios se utilizan comillas dobles dentro de la concatenacion para que no se metan con las comillas simples