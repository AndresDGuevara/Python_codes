def factorial(n):
  """
  Calcula el factorial de n.
  n int > 0
  return n!
  """
  print(n) #este imprime los pasos que hace la funcion
  if n == 1:
    return 1

  return n * factorial(n - 1)
numero = int(input('Escribe un Entero: '))
print(f'{numero}! = {factorial(numero)}')