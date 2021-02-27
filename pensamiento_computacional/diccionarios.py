import string


def run():
    mi_diccionario = {'llave1': 1, 'llave2': 2, 'llave3': 3}

    # print(mi_diccionario['llave1'])

    poblacion_paises = {
        'Colombia': 50372424, 
        'Brazil': 210147125, 
        'Argentina': 44938712
        }
    # print(poblacion_paises['Colombia'])

    # for pais in poblacion_paises.keys():
    #     print(pais)

    # for pais in poblacion_paises.values():
    #      print(pais)

    for pais, poblacion in poblacion_paises.items():
         print(pais + ' tiene ' + str(poblacion) + ' habitantes')


if __name__ == '__main__':
    run()