""" Area de un Cuadrado
"""
def Calculo1():

  l = float(input("Ingresa El Valor De Un Lado Del Cuadrado: "))
  p = l * 4 # Perimetro
  a = l * l # Area

  print("El Perimetro Es ",p," Metros")
  print("El Area Es", a, 'M²')

Calculo1()  

""" The square root of any number"""

import math
x = int(input('Enter a Number:'))

sqrt = math.sqrt(x)
print ('Square Root is:', sqrt)


""" Hypotenuse of a Pythagorean Theorem
""" 
import math
a = float(input("Enter value of A:"))
b = float(input("Enter value of B:"))

c = math.sqrt(a ** 2 + b ** 2)
print("The Value of C is:", c)

""" Area of a right triangle 
reads the length of the base and the height of a #right-angled triangle 
and prints the area. Every number is given on a separate line
"""
a = float(input('Enter Lenght of the Base:'))
b = float(input('Enter Height of the Triangle:'))

print('The Area is:', a * b / 2)

""" floor of pi elevated to e + e elevated to pi
""" 
from math import pi, e, floor

x = pi ** e + e ** pi
y = floor (x)
print (y)

"""What method could you apply to convert the complex number 
(5.74895+7j) into the integer 5?
"""
int((5.74895 + 7j).real)