""" El ordenamiento por mezcla es un algoritmo de divide y conquista. Primero divide 
una lista en partes iguales hasa que quedan sublistas de 1 o 0 elementos. Luego las 
recombina en forma ordenada
Llamada Merge Sort
O(n log (n))

"""
import random

# Esto sera un ordenamiento recursivo, esto significa que vamos a mezclar directamente 
# como ejecutamos una y otra vez la misma funcion y tambien vamos a utilizar iteraciones 
# para generar cada una de las comparaciones

# Generamos busqueda binaria dentro de la recursividad

def ordenamiento_por_mezcla(lista):
    
    if len(lista) > 1: #--- 1 seccion---
        medio = len(lista) // 2
        izquierda = lista[: medio] # desde cero a la mitar
        derecha = lista[medio :] # desde la mitad al final (slicing)
        print(izquierda, '*' * 5, derecha) #pintar la izquierda y separarlo con 5 comillas y 
                                            #despues pintar la derecha
        # Llamada recursiva en cada mitad
        # esto se va a ejecutar hasta que queden lista de un solo tamaño
        ordenamiento_por_mezcla(izquierda)
        ordenamiento_por_mezcla(derecha)
    #--- 1 seccion---

# ---2 seccion---
    # Iteradores para recorrer las dos sublistas
    # las dos primeras variables seran los iteradores para recorrer las sublistas
        i = 0
        j = 0
    # Iterador para la lista principal
        k = 0 # k es la lista intermedia 

    # Vamos a generar las primeras comparaciones entre estas dos listas

    # Aqui nos estamos asegurando que podamos comparar, si podemos comparar estamos viendo 
    # cual es el mayor y cual es el menor y dependiendo de esto estamos asignando 
    # en esta lista intermedia en el indice k [k] cada uno de los elementos

        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i] 
                i += 1
            else:
                lista[k] = derecha[j]
                j +=1

            k += 1 # Para que el while no se vaya al infinito

        while i < len(izquierda):
            lista[k] = izquierda[i] # copiate en el indice k lo que sobra de la izquierda
            i += 1 #nos movemos hacia adelante
            k += 1

        while j < len(derecha):
            lista[k] = derecha[j] # copiate en el indice k lo que sobra de la derecha
            j += 1
            k += 1
        print(f'izquierda {izquierda}, derecha {derecha}')
        print(lista) # como se esta reconstruyendo la lista con indice k
        print('-' * 50) # este nos dice que ya este paso termino 
    return lista 

if __name__ == '__main__':
    tamaño_de_lista = int(input('De que tamaño sera la lista? '))
    lista = [random.randint(0, 100) for i in range(tamaño_de_lista)]
    print(lista)
    print('-' * 20) # un divisor donde ponemos una linea por 20 veces. Vamos a generear ese string 
                        #tantas veces lo estemos multiplicando

    lista_ordenada = ordenamiento_por_mezcla(lista)
    print(lista_ordenada)


# El algoritmo tiene dos secciones:
# ---1 seccion---
# la primera nos permite subdividir las listas en listas mas pequeñas hasta que ya no tengan 
# longitud mas grande que 1, osea estan ordenadas por definicion
#tiene un crecimiento logaritmico, cada vez se vuelve mas pequeño

# ---2 seccion---
# son los while loops
# una vez que tenemos listas pequeñas las vamos a empezar comparar y lo que va quedando 
# lo compiamos para generar listas mas grandes para recombinarla y tenerlas ordenadas
