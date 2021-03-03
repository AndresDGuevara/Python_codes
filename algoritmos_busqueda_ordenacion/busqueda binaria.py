""" Esto es leer Recursividad
- si tu lista esta ordenada, usar algoritmo de busqueda binaria
- si vas a utilizar muchas veces tu lista y no esta ordenada, 
  es mejor ordenarla y utilizar algoritmo de busqueda binaria.

  La búsqueda binaria tiene una complejidad de O(log n)
  
"""
import random
def busqueda_binaria(lista, comienzo, final, objetivo):

    print(f'buscando {objetivo} entre {lista[comienzo]} y {lista[final - 1]}') # 0-

    if comienzo > final: # 1-
        return False

    medio = (comienzo + final) // 2  # 2-

    if lista[medio] == objetivo: # 3-
        return True
    elif lista[medio] < objetivo: # 4-
        return busqueda_binaria(lista, medio + 1, final, objetivo)
    else:
        return busqueda_binaria(lista, comienzo, medio - 1, objetivo) # 5-

if __name__ == '__main__':
    tamaño_de_lista = int(input('De que tamaño sera la lista: '))
    objetivo = int(input('Que numero quieres encontrar?: '))
    
    lista = sorted([random.randint(0, 100) for i in range(tamaño_de_lista)]) # 6-

    encontrado = busqueda_binaria(lista, 0, len(lista), objetivo)

    print(lista) # 7-
    
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')


# 0- con este print vemos lo que esta pasando adentro del algoritmo
#    hay una diferencia entre acceder por len y por indice y este es el famoso error de off by 1. (fallaste por uno)
#    siempre que se accede por indices si venimos de un len tenemos que restarle un -1

# 1- Caso base: si nuestro comienzo es mas grande que nuestro final quiere decir que el elemento 
#    no se encuentra en la lista. porque lo hicimos mas pequeño y mas pequeño y nos pasamos

# 2- dividir nuestra lista en dos con divicion de enteros // porque no nos interesa los decimales
#    partimos la lista para empezar las condiciones de abajo

# 3- primera condicion: si la lista en el indice medio es igual a objetivo significa que ya lo encontramos

# 4- si no, podemos pensar que la lista en el medio es menor que el objetivo, aqui es muy sencillo 
#    simplemente vamos a hacer una busqueda binaria, vamos a pasarle la lista de nuevo pero ahora comenzamos 
#    de la mitad para adelante, nuestro comienzo es medio + 1

# 5- aqui le pasamos la lista el comienzo es igual pero el final queremos que sea medio - 1 en esta condicion nos 
#    estamos llendo a la parte de abajo y le pasamos el objetivo

# 6- La busqueda binaria asume que la lista esta ordenara entonces es aqui donde se ordena
#    sorted organiza la lista 
#    vamos a utilizar indices para irnos moviendo adentro de la misma lista, en lugar de ir haciendo listas cada vez 
#    mas pequeñas empezamos en 0 y terminamos en la lonjitud de la lista (len) y vamos a ver cual es el objetivo

# 7- imprimimos la lista para saber que esta sucediendo con los numeros aleatorios