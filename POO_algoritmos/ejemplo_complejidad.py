import math

class complejidad_algoritmica():
    def __init__(self, n):
        self.n = n

    def constante(self):
        return 1

    def lineal(self):
	    return self.n

    def logaritmica(self):
        return math.log10(self.n)

    def log_lineal(self):	
	    return self.n * math.log10(self.n)

    def	polinomial(self):
    	return self.n ** 2

    def	exponencial(self):
    	return 2 ** self.n

def main():
    menu = """
    para entender mejor el BIG O NOTATION
    
    a. 10
    b. 100
    c. 1000

    Elije una opción de esta lista: """
    
    while True:
        opcion = input(menu).strip()
        if opcion == 'a':
            complejidad = complejidad_algoritmica(10)
        elif opcion == 'b':
            complejidad = complejidad_algoritmica(100)
        elif opcion == 'c':
            complejidad = complejidad_algoritmica(1000)
        else:
            print('Elige una opción válida: a, b, c')
            continue

        print(f'O(1) es {complejidad.constante()}')
        print(f'O(n) es igual {complejidad.lineal()}')

        print(f'O(log n) es {complejidad.logaritmica()}')
        print(f'O(n log n) es {complejidad.log_lineal()}')

        print(f'O(n**2) es igual a {complejidad.polinomial()}')
        print(f'O(2**n) es igual a {complejidad.exponencial()}')
        break

if __name__ == '__main__':
    main()


# import math

# menu = """
# Elije un número de esta lista:
# 10
# 100
# 1000
# para entender mejor el 
# BIG O NOTATION
# """

# opcion = int(input(menu))

# if opcion == 10:
#     print(f'O(1) es {1}')
#     print(f'O(log n) es {math.log(opcion)}')
#     print(f'O(n log n) es {math.log10(opcion)}')
#     print(f'O(n) es igual {opcion}')
#     print(f'O(n**2) es igual a {opcion**2}')
#     print(f'O(2**n) es igual a {2**opcion}')


# elif opcion == 100:
#     print(f'O(1) es {1}')
#     print(f'O(log n) es {math.log(opcion)}')
#     print(f'O(n log n) es {math.log10(opcion)}')
#     print(f'O(n) es igual {opcion}')
#     print(f'O(n**2) es igual a {opcion**2}')
#     print(f'O(2**n) es igual a {2**opcion}')


# elif opcion == 1000:
#     print(f'O(1) es {1}')
#     print(f'O(log n) es {math.log(opcion)}')
#     print(f'O(n log n) es {math.log10(opcion)}')
#     print(f'O(n) es igual {opcion}')
#     print(f'O(n**2) es igual a {opcion**2}')
#     print(f'O(2**n) es igual a {2**opcion}')

# else:
#     print('Elige una opción válida: 10, 100, 1000... NO MAMES HUEVÓN')


