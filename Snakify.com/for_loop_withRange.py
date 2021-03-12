""" Series - 1:
    given two integers A and B (≤ B). Print all numbers from A to B inclusively."""
a = int(input())
b = int(input())
for i in range (a, b + 1):
    print(i)

""" Series - 2:
Given two integers A and B. Print all numbers from A to B inclusively, in ascending order, if A < B, or in descending order, if A ≥ B.
"""
a = int(input())
b = int(input())
if a < b:
    for i in range(a, b + 1):
        print(i)
else:
    for i in range(a, b - 1, -1):
        print(i)

""" Sum of ten numbers:
10 numbers are given in the input. Read them and print their sum. Use as few variables as you can.
"""
a = 0
answer = 0
for i in range(10):
    i = int(input())
    answer += i
print(answer)

""" or """
res = 0
for i in range(10):
    res += int(input())
print(res)

""" Sum of N numbers:
N numbers are given in the input. Read them and print their sum.
The first line of input contains the integer N, which is the number of integers to follow. Each of the next N lines contains one integer. Print the sum of these N integers.
"""
N = int(input())
answer = 0
for i in range(N):
    answer += int(input())
print(answer)

""" Sum of Cubes:
For the given integer N calculate the following sum:
1 ** 3 + 2 ** 3 + … + N ** 3
"""
n = int(input())
answer = 0
for i in range(n + 1):
    answer += i ** 3
print(answer)

""" or """
res = 0
for i in range(1, int(input()) + 1):
    res += i ** 3
print(res)

""" Factorial:
In mathematics, the factorial of an integer n, denoted by n! is the following product:
n != 1 × 2 × … × n
For the given integer n calculate the value n!. Don't use math module in this exercise.
"""
n = int(input())
answer = 1
for i in range(n):
    answer = answer * (i + 1)
print(answer)

""" or """
res = 1
n = int(input())
for i in range(1, n + 1):
    res *= i
print(res)

""" The numbers of zeros:
Given N numbers: the first number in the input is N, after that N integers are given. Count the number of zeros among the given integers and print it.
You need to count the number of numbers that are equal to zero, not the number of zero digits.
"""
n = int(input())
answer = 0
for i in range(n):
    n = int(input())
    if n == 0:
        answer += 1
print(answer)

""" or """
num_zeroes = 0
for i in range(int(input())):
    if int(input()) == 0:
        num_zeroes += 1
print(num_zeroes)

""" Adding Factorial:
Given an integer n, print the sum 1! + 2! + 3! + ... + n!.
This problem has a solution with only one loop, so try to discover it. And don't use the math library :)
"""
b = 0
a = 1
n = int(input())
for k in range(1, n + 1):
    a = 1
    for i in range (1 , k + 1):
        a = i * a 
    b = b + a
print(b)

""" or """
n = int(input())
partial_factorial = 1
partial_sum = 0
for i in range(1, n + 1):
    partial_factorial *= i
    partial_sum += partial_factorial
print(partial_sum)

""" Ladder:
For given integer n ≤ 9 print a ladder of n steps. The k-th step consists of the integers from 1 to k without spaces between them.
To do that, you can use the sep and end arguments for the function print().
"""
answer = ""
n = int(input())
for i in range(n):
    answer += str(i + 1)
    print(answer)

""" or """
n = int(input())
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, sep='', end='')
    print()

""" Lost Card:
There was a set of cards with numbers from 1 to N. One of the card is now lost. Determine the number on that lost card given the numbers for the remaining cards.
Given a number N, followed by N − 1 integers - representing the numbers on the remaining cards (distinct integers in the range from 1 to N). Find and print the number on the lost card
"""
answer = 0
N = int(input())
N_org = N
for i in range(N - 1):
    N = int(input())
    answer += N
for i in range(N_org):
    N_org += i
    i += 1
N_org -= answer
print(N_org)

""" or """
n = int(input())
sum_cards = 0
for i in range(1, n + 1):
    sum_cards += i
# One can prove the following:
# sum_cards == n * (n + 1) // 2
# However, we'll calculate that using the loop.
for i in range(n - 1):
    sum_cards -= int(input())
print(sum_cards)

