"""Last digit of integer:
Given an integer number, print its last digit.
"""
a = int(input())
int = a % 10
print(int)
"""or"""
a = int(input())
print(a % 10)

"""Tens digit:
Given an integer. Print its tens digit.
"""
a = int(input())
print(a // 10 % 10)

"""Sum of digits:
Given a three-digit number. Find the sum of its digits
"""
a = int(input())
x  = a // 1000
x1 = (a - x * 1000) // 100
x2 = (a - x * 1000 - x1 * 100) //10
x3 = (a - x * 1000 - x1 * 100 - x2 * 10)
print(x + x1 + x2 + x3)

"""or"""
n = int(input())
a = n // 100
b = n // 10 % 10
c = n % 10
print(a + b + c)

"""Fractional part:
Given a positive real number, print its fractional part.
"""
a = float(input())
print (a % 1)

"""First digit after decimal point:
Given a positive real number, print its first digit to the right of the decimal point.
"""
a = float(input())
import math
frac = math.modf(a)
frac1 = str(frac[0])
print(frac1 [2])

"""or"""
x = float(input())
print(int(x * 10) % 10)

"""Car route:
A car can cover distance of N kilometers per day. How many days will it take to cover
a route of length M kilometers? The program gets two numbers: N and M.
"""
N = int(input())
M = int(input())
O= M % N
if O != 0:
  p = int((M / N) + 1)
  print(p)
else:
  P= int(M / N)
  print(P)

"""or"""
from math import ceil

n = int(input())
m = int(input())
print(ceil(m / n))

"""Digital clock:
Given the integer N - the number of minutes that is passed since midnight - how many hours 
and minutes are displayed on the 24h digital clock?
The program should print two numbers: the number of hours (between 0 and 23) and the number of minutes (between 0 and 59).

For example, if N = 150, then 150 minutes have passed since midnight - i.e. now is 2:30 am. So the program should print 2 30.
"""
a = int(input())
print(((a // 60) % 60),(a % 60))

"""or"""
n = int(input())
hours = n // 60
minutes = n % 60
print(hours, minutes)

"""Total cost:
A cupcake costs A dollars and B cents. Determine, how many dollars and cents should one pay for N cupcakes. A program gets 
three numbers: A, B, N. It should print two numbers: total cost in dollars and cents.
"""
a = int(input())
b = int(input())
n = int(input())
print((n * a * 100 + n * b) // 100,( n * a * 100 + n * b) % 100)

"""or"""
a = int(input())
b = int(input())
n = int(input())
cost = n * (100 * a + b)
print(cost // 100, cost % 100)

"""Clock face - 1:
H hours, M minutes and S seconds are passed since the midnight (0 ≤ H < 12, 0 ≤ M < 60, 0 ≤ S < 60). Determine the angle 
(in degrees) of the hour hand on the clock face right now.
"""
a = int(input())
b = int(input())
c = int(input())
x = (360 / 12) * a
y = (360 / 12 / 60) * b
z = (360 / 12 / 60 / 60) * c 
s = x + y + z
print(s)

"""or"""
h = int(input())
m = int(input())
s = int(input())
print(h * 30 + m * 30 / 60 + s * 30 / 3600)

"""Clock face - 2:
Hour hand turned by α degrees since the midnight. Determine the angle by which minute hand turned since the start of 
the current hour. Input and output in this problems are floating-point numbers.
"""
a = float(input())
print(a % 30 * 12)