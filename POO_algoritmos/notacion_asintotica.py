"""conteo abstracto de operarion"""
def f(x):
    respuesta = 0 #primer operacion

    for i in range(1000): #este loop no depende de x, segunda operacion
        respuesta += 1
        #respuesta = 0
    for i in range(x): # este loop depende de x 
        respuesta += x

    for i in range(x):
        for j in range(x):
            respuesta += 1
            respuesta += 1

    return respuesta #tercera operacion


""" Ley de la Suma"""
# Dos codigos con crecieminto lineal
def f(n):
  
  for i in range(n):
    print(i)

#lo que mas va a importar es este loop conforme nos acercamos al infinito
  for i in range(n * n): 
    print(i)

# 0(n) + 0(n * n) = 0(n + n^2) = 0(n^2)
#Esta creciendo en n al cuadrado
#en big o solo importa el termino mas grande

                    # Ley de la suma
def f(n):

  for i in range(n):
    print(i)

  for i in range(n):
    print(i)

# o(n) + o(n) = o(n + n) = o(2n) = o(n)
# La funcion crece en o de n 

"""Ley de la multipliacion"""
# Crecieminto Cuadratico 
def f(n):
  
  for i in range(n):
#loop dentro de otro loop, donde se multiplican los dos terminos (n)
    for j in range(n):
      print(i, j)

#0(n) * 0(n) = 0(n * n) = 0(n^2)
# esto es un crecimiento cuadratico por ser un loop dentro de otro loop

"""Recursividad multiple"""
# Crecieminto exponencial
def fibonacci(n):
#primera llamada
  if n == 0 or n == 1:
    return 1
#dos llamadas generadas
  return fibonacci(n - 1) + fibonacci(n - 2)

#0(2 ** n)
#Algoritmo de fibonacci recursivo
#Por cada llamada de fibonacci estamos generando dos llamadas de fibonacci
# Esto es un crecimiento exponencial por ser llamdas recursivas