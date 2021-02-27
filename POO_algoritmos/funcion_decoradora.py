def funcion_decoradora(parametro):

    def funcion_interna():
        print("Hagamos un calculo")
                #Aqui es donde se agrega la logica que va
                # a ser añadida a la funcion
        parametro()

        print("Hemos hecho el calculo")
    return funcion_interna

@funcion_decoradora #Aqui es donde se le agrega la decoracion,
                    # la funcion que queramos
def suma():
    print(15 + 20)

@funcion_decoradora
def resta():
    print(30 - 10)

suma()
resta()