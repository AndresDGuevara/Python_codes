"""Afirmaciones
asserts. Programacion defensiva para evitar bugs
assert <expresion booleana>, <mensaje de error>"""

def primera_letra(lista_de_palabras):
    primera_letras = []

    for palabra in lista_de_palabras:
        assert type(palabra) == str, f'{palabra} no es str'
        assert len(palabra) > 0, 'No se permiten str vacios'

        primera_letras.append(palabra[0])
    return primera_letras

lista_de_palabras = ['vaso', 'billetera', 'cargador']
palabras = list(primera_letra(lista_de_palabras)) # Convirtiendo una funcion en lista
print(palabras)
