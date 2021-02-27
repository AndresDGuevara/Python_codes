def enumeracion_exhaustiva(objetivo):
    respuesta = 0
    
    while respuesta ** 2 < objetivo:
        #print(respuesta)
        respuesta += 1

    if respuesta ** 2 == objetivo:
        print(f'La raiz cuadrada de {objetivo} es {respuesta}')
    else:
        print(f'{objetivo} no tiene una raiz cuadrada exacta')


def aproximacion(objetivo):
    epsilon = 0.01
    paso = epsilon ** 2 
    respuesta = 0.0

    while abs(respuesta ** 2 - objetivo) >= epsilon and respuesta <= objetivo: #este ultimo bloque nos evita calular negativos
        #print(abs(respuesta ** 2 - objetivo), respuesta)
        respuesta += paso

    if abs(respuesta ** 2 - objetivo) >= epsilon:
        print(f'No se encontro la raiz cuadrada {objetivo}')
    else:
        print(f'La raiz cudrada de {objetivo} es {respuesta}')


def busqueda_binaria(objetivo):
    epsilon = 0.01
    bajo = 0.0
    alto = max(1.0, objetivo)
    respuesta = (alto + bajo) / 2

    while abs(respuesta ** 2 - objetivo) >= epsilon:
        #print(f'bajo={bajo}, alto={alto}, respuesta={respuesta}')
        if respuesta ** 2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta
        respuesta = (alto + bajo) / 2

        print(f'La raiz cuadrada de {objetivo} es {respuesta}')


def run():
    print("Bienvenidos! Calculemos la raiz cuadrada de un numero\n")

    objetivo = int(input("Ingresa el numero entero que deseas calcular: "))

    menu = f"""A continuacion Escoge una de las siguientes opciones para calcular {objetivo}:
    1- Enumeracion Exhaustiva 
    2- Aproximacion  
    3- Busqueda Binaria 

    Elige una opcion: """
    opcion = int(input(menu)) 
    
    if opcion == 1:
        enumeracion_exhaustiva(objetivo)
    elif opcion == 2:
        aproximacion(objetivo)
    elif opcion == 3:
        busqueda_binaria(objetivo)
    else:
        print("Ingresa una opcion valida")

    while True:
        print("\n\t¿Desea Continuar? \n SI = 1\n NO = 2\n")
        opcion = int(input(': '))
        if opcion == 1:
            respuesta = True
            run()
        else:
            respuesta = False
            print("\n Gracias, que tengas un buen dia")
        break


if __name__ == '__main__':
    run()