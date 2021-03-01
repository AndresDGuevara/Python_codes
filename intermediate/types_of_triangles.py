""" Write a function that accepts 3 sides of a triangle and returns the type of the triangle
Types of triangle -
 1. Equilateral triangle -> All the 3 sides are equal (Ex: 10, 10, 10)
 2. Isosceles triangle -> 2 sides are equal (Ex: 10, 10, 20)
 3. Scalene triangle -> No sides are equal (Ex: 10, 20, 30)
"""
def TypeOfTriangle (a,b,c):
  if a != b and b != c and a != c:
    print('The Type of Triangle is: Scalene triangle')
    return c
  elif a == b == c:
    print('The Type of Triangle is: Equilateral triangle')
    return a
  else:
    print('The Type of Triangle is: Isosceles triangle')
    return b

print('Enter Three sides of a Triangle Below:')
a = int(input('First Side: '))
b = int(input('Second Side: '))
c = int(input('Third Side: '))

TypeOfTriangle = TypeOfTriangle (a,b,c)