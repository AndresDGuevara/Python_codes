   # def suma(a, b):
    #    print('Se suman dos números')
     #   resultado = a + b
      #  return resultado

    #sumatoria = suma(1, 4)
    #print(sumatoria


def conversor(tipo_pesos, valor_dolar):
    pesos = input("Cuantos pesos " + tipo_pesos + " tienes?: ")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")

def run():
    menu = """
    Bienvenido al conversor de monedas ðŸ’°

    1 - Pesos colombianos
    2 - Pesos argentinos
    3 - Pesos mexicanos

    Elige una opción: """

    opcion = int(input(menu))

    if opcion == 1:
        conversor("colombianos", 3875) 
    elif opcion == 2:
        conversor("argentinos", 65)
    elif opcion == 3:
        conversor("mexicanos", 24)
    else:
        print('Ingresa una opción correcta por favor')


if __name__ == '__main__':
    run()