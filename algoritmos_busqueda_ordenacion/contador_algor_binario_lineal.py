import random
import time

def busqueda_lineal(lista_l, objetivo, iteracion_lineal = 0):
    match = False

    for elemento in lista_l:      
        iteracion_lineal += 1
        if elemento == objetivo:
            match = True
            break
    return (match, iteracion_lineal)


def busqueda_binaria (lista, comienzo, final, objetivo, iteracion_binaria = 0):
    #print(f'Buscando {objetivo} entre {comienzo} y {final_lineal}')
    iteracion_binaria += 1

    if comienzo > final:
        return (False, iteracion_binaria)
        
    medio = (comienzo + final) // 2
    
    if lista[medio] == objetivo:
        return (True, iteracion_binaria)
    elif lista[medio] < objetivo:
        return busqueda_binaria(lista, medio + 1, final, objetivo, iteracion_binaria = iteracion_binaria)
    else:
        return busqueda_binaria(lista, comienzo, medio - 1, objetivo, iteracion_binaria = iteracion_binaria)
        

if __name__  ==   '__main__':

    tamano_de_lista = int(input('De que tamano sera la lista?: '))
    objetivo = int(input('Que numero quieras encontrar?: '))
    
    print("\n-----Busqueda Lineal-----")
    lista_l = [random.randint(0, 100) for i in range(tamano_de_lista)]
    print(lista_l)
    comienzo_lineal = time.time()
    (encontrado_lineal, iteracion_lineal) = busqueda_lineal(lista_l, objetivo)
    final_lineal = time.time()
    print(f'El elemento {objetivo} {"esta" if encontrado_lineal else "no esta"} en la lista')
    print(f'Las Iteraciones fueron: {iteracion_lineal}')
    print(f'El tiempo Lineal fue de: {(final_lineal - comienzo_lineal)}')
    
    print("\n-----Busqueda Binaria-----")
    lista_b = sorted([random.randint(0, 100) for i in range(tamano_de_lista)])
    print(lista_b)
    comienzo_binario = time.time()
    (encontrado_binario, iteracion_binaria) = busqueda_binaria(lista_b, 0, len(lista_b), objetivo)
    final_binario = time.time()
    print(f'El elemento {objetivo} {"esta" if encontrado_binario else "no esta"} en la lista')
    print(f'Las Iteraciones fueron: {iteracion_binaria}')
    print(f'El tiempo binario fue de {(final_binario - comienzo_binario)}')