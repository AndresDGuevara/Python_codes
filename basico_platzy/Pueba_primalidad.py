# def es_primo(numero):
#     contador = 0
#     for i in range(1, numero + 1):
#         if i == 1 or i == numero:
#             continue
#         elif numero % i == 0:
#             contador += 1
#     if contador == 0:
#         return True
#     else:
#         return False 


# def run():
#     numero = int(input('Escribe un numero: '))
#     if es_primo(numero):
#         print('Es primo')
#     else:
#         print('No es primo')



# def run():
#     numero = int(input('Escribe un numero: '))
#     if numero > 1:
#         for a in range(2, numero):
#             if (numero % a) == 0:
#                 print(numero, "No es numero primo")
#                 break
#         else:
#             print(numero, "Es un numero primo")


def run():
    print("""TODOS LOS NUMEROS PRIMOS EN UN INTERVALO""")

    minimo = int(input("\nEscribe el numero menor: "))
    maximo = int(input("Escribe el numero mayor: "))

    print("\nTODOS Los numeros primos en el intervalo entre", minimo, "y", maximo, "son: ")
    
    for numero in range(minimo, maximo + 1):
        if numero > 1:
            for a in range(2, numero):
                if (numero % a) == 0:
                    break
            else:
                print(numero)

if __name__ == '__main__':
    run()