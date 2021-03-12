"""Minimum of two numbers:
Given two integers, print the smaller value.
"""
a = int(input())
b = int(input())
if a > b: 
    if b > a:
        print(a)
    else:
        print(b)
else:
    if b < a:
        print(b)
    else:
        print(a)

"""or"""
a = int(input())
b = int(input())
if a < b:
    print(a)
else:
    print(b)

"""Sign function:
For the given integer X print 1 if it's positive, -1 if it's negative, or 0 if it's equal to zero.
Try to use the cascade if-elif-else for it
"""
x = int(input())
if x > 0:
    print(1)
elif x < 0:
    print(-1)
else:
    print(0)

"""or"""
x = int(input())
if x > 0:
    print(1)
elif x == 0:
    print(0)
else:
    print(-1)

"""Minimum of three numbers:
Given three integers, print the smallest value
"""
a = int(input())
b = int(input())
c = int(input())
if a < b and a < c:
    print(a)
elif b < c:
    print(b)
else:
    print(c)

"""or"""
a = int(input())
b = int(input())
c = int(input())
if b >= a <= c:
    print(a)
elif a >= b <= c:
    print(b)
else:
    print(c)

"""Equal numbers:
Given three integers, determine how many of them are equal to each other. The program must print 
one of these numbers: 
3 (if all are the same), 2 (if two of them are equal to each other and the third is different) 
or 0 (if all numbers are different).
"""
a = int(input())
b = int(input())
c = int(input())
if a != b and b != c and a != c:
    print(0)
elif a == b == c:
    print(3)
else:
    print(2)

"""or"""
a = int(input())
b = int(input())
c = int(input())
if a == b == c:
    print(3)
elif a == b or b == c or a == c:
    print(2)
else:
    print(0)

""" Leap year:
Given the year number. You need to check if this year is a leap year. If it is, print LEAP, otherwise print COMMON.
The rules in Gregorian calendar are as follows:

a year is a leap year if its number is exactly divisible by 4 and is not exactly divisible by 100
a year is always a leap year if its number is exactly divisible by 400
Warning. The words LEAP and COMMON should be printed all caps.
"""
year = int(input())
if ( year % 400 == 0) or ( year % 4 == 0 ) and ( year % 100 != 0):
    print(" LEAP ")
else:
    print(" COMMON")

"""Chocolate bar:
Chocolate bar has the form of a rectangle divided into n×m portions. Chocolate bar can be split into two rectangular parts by breaking it along a selected straight line on its pattern. Determine whether it is possible to split it so that one of the parts will have exactly k squares.
The program reads three integers: n, m, and k. It should print YES or NO.
"""
n = int(input())
m = int(input())
k = int(input())

if (k % n == 0 and k / n < m) or (k % m == 0 and k / m < n):
    print('YES')
else:
    print('NO')

"""or"""
n = int(input())
m = int(input())
k = int(input())
if k < n * m and ((k % n == 0) or (k % m == 0)):
    print('YES')
else:
    print('NO')
"""
"""
