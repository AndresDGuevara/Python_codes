from typing import List


def divide_elementos_de_lista(lista, divisor):
    """try y except
     permiten asegurarte que no vamos a tener errores dentro del codigo
     y permite manejar estas excepciones para que mi codigo no falle 
     cuando nos encontremos con uno de estos errores"""
    try: 
        return [i / divisor for i in lista]
    except ZeroDivisionError as e:
        print(e)
        return lista

lista = list(range(10))
divisor = 0

print(divide_elementos_de_lista(lista, divisor))