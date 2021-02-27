def palindromo(palabra):
    palabra = palabra.replace(' ', '') #Elimina espacios
    palabra = palabra.lower() #Cambia caracteres a minuzcula
    palabra_invertida = palabra[::-1] #desde el final hasta el principio de pasos de uno
    if palabra == palabra_invertida:
        return True
    else:
        return False
    

def run():
    palabra = input('Escribe una palabra: ')
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print('Es Palindromo')
    else:
        print('No es palindromo')


if __name__ == '__main__':
    run()