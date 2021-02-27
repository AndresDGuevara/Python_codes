"""Sum of three numbers:
Write a program that takes three numbers and prints their sum. 
Every number is given on a separate line
"""
a = int(input())
b = int(input())
c = int(input())
s = a + b + c 
print(s)

"""Hi John:
Write a program that greets the person by printing the word 
"Hi" and the name of the person
"""
name = input ()
print ('Hi', name)

"""Square:
Write a program that takes a number and print its square"""
a = int (input())
print (a ** 2)

"""Area of right_angled triangle:
Write a program that reads the length of the base and the height of a right-angled 
triangle and prints the area. Every number is given on a separate line.
"""
a = int(input())
b = int(input())
s = a * b / 2
print (s)

"""Hello Harry! :
Write a program that greets the user by printing the word "Hello", a comma, 
the name of the user and an exclamation mark after it. See the examples below.

Warning. Your program's output should strictly match the desired one, character 
by character. There shouldn't be any space between the name and the exclamation mark. 
You can use + operator to concatenate two strings. See the lesson for details.
"""
name = input ()
print ('Hello'',' , name + '!')
"""or"""
print('Hello, ' + input() + '!')

"""Apple Sharing:
N students take K apples and distribute them among each other evenly. The remaining
(the undivisible) part remains in the basket. How many apples will each single student get?
How many apples will remain in the basket?
The program reads the numbers N and K. It should print the two answers for the questions above
"""
n = int (input())
k = int (input())
print (k // n )
print (k % n)

"""Previous and next:
Write a program that reads an integer number and prints its previous and next numbers. 
See the examples below for the exact format your answers should take. There shouldn't be a 
space before the period.
Remember that you can convert the numbers to strings using the function str
"""
a = int (input())
print ('The next number for the number', a, 'is', str (a + 1) + '.')
print ('The previous number for the number', a, 'is', str (a - 1) + '.')

"""Two timestamps:
A timestamp is three numbers: a number of hours, minutes and seconds. Given two timestamps,
calculate how many seconds is between them. The moment of the first timestamp occurred
before the moment of the second timestamp
"""
hours1 = int(input()) 
minutes1 = int(input())
seconds1 = int(input())
hours2 = int(input())
minutes2 = int(input()) 
seconds2 = int(input())
total1 = minutes1 * 60 + hours1 * 3600 + seconds1 
total2 = minutes2 * 60 + hours2 * 3600 + seconds2 
print(total2 - total1)

"""or"""
hours_1 = int(input())
minutes_1 = int(input())
seconds_1 = int(input())
hours_2 = int(input())
minutes_2 = int(input())
seconds_2 = int(input())
print(hours_2 * 3600 + minutes_2 * 60 + seconds_2
    - hours_1 * 3600 - minutes_1 * 60 - seconds_1)

"""School desks:
A school decided to replace the desks in three classrooms. Each desk sits two students. 
Given the number of students in each class, print the smallest possible number of desks that can be purchased.
The program should read three integers: the number of students in each of the three classes, a, b and c respectively.

In the first test there are three groups. The first group has 20 students and thus needs 10 desks. 
The second group has 21 students, so they can get by with no fewer than 11 desks. 11 desks is also enough 
for the third group of 22 students. So we need 32 desks in total
"""
a = int(input())
b = int(input())
c = int(input())
print(a // 2 + b // 2 + c // 2 + a % 2 + b % 2 + c % 2)