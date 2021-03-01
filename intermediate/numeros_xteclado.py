"""Realiza un programa que lea dos números por teclado y permita elegir entre 3 opciones en un menú:

Mostrar una suma de los dos números
Mostrar una resta de los dos números (el primero menos el segundo)
Mostrar una multiplicación de los dos números

En caso de no introducir una opción válida, el programa informará de que no es correcta.
"""
    
a = float(input('\n Ingrese primer numero: '))
b = float(input('Ingrese segundo numero: '))

print('¿Que quieres hacer?')
print('[1] sumar los dos numeros: ')
print('[2] restar los dos numeros:')
print('[3] multiplicar los dos numeros: ')

opcion = input('introduce una opcion: ')

if opcion =='1':
    print('La suma de',a,'+',b,'es',a + b)
elif opcion =='2':
    print('La resta de',a,'-',b,'es', a - b)
elif opcion =='3':
      print('La multipliccion de',a,'*',b,'es', a * b)
else:
    print('La informacion no es correcta')