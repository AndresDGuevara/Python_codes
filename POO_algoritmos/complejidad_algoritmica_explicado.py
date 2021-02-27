import math
import time 

class Complejidad_algoritmica:
	def __init__(self, n):
		self.n = n

	def constante(self):
		return 1

	def logaritmica(self):
		return math.log10(self.n)

	def lineal(self):
		return self.n

	def log_lineal(self):	
		return self.n * math.log10(self.n)

	def	polinomial(self):
		return self.n ** 2

	def	exponencial(self):
		return 2 ** self.n


def main():
	
    nums = [1, 10, 100, 1000, 10000]
    
    for n in nums:
        
        complejidad = Complejidad_algoritmica(n)
        
        print('n es igual a: {}'.format(n))
        
        principio = time.time()
        print(f'El resultado de complejidad constante para n igual a {n} es: ', complejidad.constante())
        fin = time.time()
        tiempo = fin - principio
        print(f'has tardado {tiempo} segundos\n')
        
        principio = time.time()
        print(f'El resultado de complejidad logaritmica para n igual a {n} es: ', complejidad.logaritmica())
        fin = time.time()
        tiempo = fin - principio
        print(f'has tardado {tiempo} segundos\n')
        
        principio = time.time()
        print(f'El resultado de complejidad lineal para n igual a {n} es: ', complejidad.lineal())
        fin = time.time()
        tiempo = fin - principio
        print(f'has tardado {tiempo} segundos\n')
        
        principio = time.time()
        print(f'El resultado de complejidad logaritmica lineal para n igual a {n} es: ', complejidad.log_lineal())
        fin = time.time()
        tiempo = fin - principio
        print(f'has tardado {tiempo} segundos\n')
        
        principio = time.time()
        print(f'El resultado de complejidad polinomial para n igual a {n} es: ', complejidad.polinomial())
        fin = time.time()
        tiempo = fin - principio
        print(f'has tardado {tiempo} segundos\n')
       
        principio = time.time()
        print(f'El resultado de complejidad exponencial para n igual a {n} es: ', complejidad.exponencial())
        fin = time.time()
        tiempo = fin - principio
        print(f'has tardado {tiempo} segundos\n')
        
        print('\n\n')
        

if __name__ == '__main__':
    main()


"""Aqui con un loop mas corto que el anterior"""
#  i = 0
#  for numbers in n:
#         print(num(n[i]))
#         print(logarithm(n[i]))
#         print(lineal(n[i]))
#         print(n_logarithm(n[i]))
#         print(square(n[i]))
#         print(exponential(n[i]))
#         print('\n')
#         i+=1

"""Otro loop mas de ejemplo"""
# values = [10, 100, 1000]
# for v in values:
#     print(f'With {v}')
#     print(f'Constant: {O_constant(v)}')
#     print(f'Log n: {O_log_n(v)}')
#     print(f'Lineal: {O_lineal(v)}')
#     print(f'n log n: {O_lineal_log_n(v)}')
#     print(f'Polynomial: {O_polynomial(v)}')
#     print(f'Exponencial: {O_exponencial(v)}')
#     print(f'---------------------------------')