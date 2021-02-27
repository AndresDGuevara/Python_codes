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

"""
"""