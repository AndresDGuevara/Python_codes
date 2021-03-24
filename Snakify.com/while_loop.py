"""List of squares:
For a given integer N, print all the squares of integer numbers where the 
square is less than or equal to N, in ascending order.
"""
n = int(input())
i = 1
for i in range(1 , n +1):
    if i ** 2 <= n:
        print(i ** 2)
    
""" or better """
n = int(input())
i = 1
while i ** 2 <= n:
    print(i ** 2)
    i += 1

""" Least divisor:
Given an integer not less than 2. Print its smallest integer divisor greater than 1.
"""
x = int(input())

if x >= 2:
  for i in range(2, x + 1):
    if x % i == 0:
        print(i)
        break

""" or better """
n = int(input())
i = 2
while n % i != 0:
    i += 1
print(i)

""" The power of two:
For a given integer N, find the greatest integer x where 2x is less than or equal to N. 
Print the exponent value and the result of the expression 2x.
Don't use the operation **.
"""
x = int(input())
n = 0

while 2 ** n <= x:
  n += 1
print (n - 1)
print (2 ** (n - 1))

""" or better """

n = int(input())
two_in_power = 2
power = 1
while two_in_power <= n:
    two_in_power *= 2
    power += 1
print(power - 1, two_in_power // 2)

""" Morning jog:
As a future athlete you just started your practice for an upcoming event. Given that on 
the first day you run x miles, and by the event you must be able to run y miles.
Calculate the number of days required for you to finally reach the required distance for
the event, if you increases your distance each day by 10% from the previous day.

Print one integer representing the number of days to reach the required distance.
"""
x = int(input())
y = int(input())
d = 1
while x < y:
  x += x * 0.1
  d += 1
print(d)

""" or """
x = int(input())
y = int(input())
i = 1
while x < y:
    x *= 1.1
    i += 1
print(i)

""" The length of the sequence: 
Given a sequence of non-negative integers, where each number is written in a separate line. 
Determine the length of the sequence, where the sequence ends when the integer is equal to 0. 
Print the length of the sequence (not counting the integer 0).
The numbers following the number 0 should be omitted.
"""
n = int(input())
len = 0
while n != 0:
    len += 1
    n = int(input())
print(len)

""" or better """
len = 0
while int(input()) != 0:
    len += 1
print(len)

""" The sum of the sequence:
Determine the sum of all elements in the sequence, ending with the number 0.
"""
sum = 0
n = int(input())
while n != 0:
    sum += n
    n = int(input())
print(sum)

""" The average of the sequence:
Determine the average of all elements of the sequence ending with the number 0
"""
e = int(input())
len = 0
sum = 0
while e != 0:
    sum += e
    len += 1
    e = int(input())
print(sum / len)

""" The maximum of the sequence:
A sequence consists of integer numbers and ends with the number 0. 
Determine the largest element of the sequence.
"""
e = int(input())
numbers = []
while e != 0:
    numbers.append(e)
    e = int(input())
print(max(numbers))

""" or """
max = 0
element = -1
while element != 0:
    element = int(input())
    if element > max:
        max = element
print(max)

""" The index of the maximum of a sequence:
A sequence consists of integer numbers and ends with the number 0. 
Determine the index of the largest element of the sequence. 
If the highest element is not unique, print the index of the first of them. 
"""
n = int(input())
max = n
index = 1
max_index = 1
while n != 0:
    n = int(input())
    index += 1
    if n > max:
        max = n
        max_index = index
print(max_index)

""" or """
max = 0
index_of_max = -1
element = -1
len = 1
while element != 0:
    element = int(input())
    if element > max:
        max = element
        index_of_max = len
    len += 1
print(index_of_max)

# This one will look for the max index of a sequence of integer
# numbers

e = int(input())
numbers = []
while e != 0:
    numbers.append(e)
    max_value = max(numbers)
    e = int(input())
    max_index = numbers.index(max_value)
print(max_index)

""" The number of even elements of the sequence:
Determine the number of even elements in the sequence ending with the number 0.
"""
e = int(input())
count = 0
while e != 0:
    if e % 2 == 0:
        count += 1
    e = int(input())
print(count)

""" or """
num_even = -1
element = -1
while element != 0:
    element = int(input())
    if element % 2 == 0:
        num_even += 1
print(num_even)

""" The number of elements that are greater than the previous one: 
A sequence consists of integer numbers and ends with the number 0. 
Determine how many elements of this sequence are greater than their neighbours above.
"""
e = int(input())
lst = []
count = 0
while e != 0:
    lst.append(e)
    e = int(input())
for i in range(1, len(lst)):
    if lst[i] > lst[i - 1]:
        count += 1
print(count)

""" or better """
prev = int(input())
answer = 0
while prev != 0:
    next = int(input())
    if next != 0 and prev < next:
        answer += 1
    prev = next
print(answer)

""" The second maximum:
The sequence consists of distinct positive integer numbers and ends with the number 0. 
Determine the value of the second largest element in this sequence. It is guaranteed 
that the sequence has at least two elements.
"""
e = int(input())
lst = []

while e != 0:
  lst.append(e)
  e = int(input())

lst = [int(e) for e in lst]
lst.sort()

print(lst[-2])

""" A peace of weird code:
"""
max = 0
e = -1
while e != 0:
    e = int(input())
    if e > max and e == 1:
        max = e
    elif max >= 1:
        print(e)
print(max)

""" The number of elements equal to the maximum: 
A sequence consists of integer numbers and ends with the number 0. 
Determine how many elements of this sequence are equal to its largest element.
"""
e = int(input())
lst = []
s = ""

while e != 0:
  lst.append(e)
  s += str(e)
  e = int(input())
  
print(s.count(str(max(lst))))

""" or """
maximum = 0
num_maximal = 0
element = -1
while element != 0:
    element = int(input())
    if element > maximum:
        maximum, num_maximal = element, 1
    elif element == maximum:
        num_maximal += 1        
print(num_maximal)

""" Fibonacci numbers:
The Fibonacci sequence is defined as follows:
ϕ0 = 0, ϕ1 = 1, ϕn = ϕn−1 + ϕn−2.
Given a non-negative integer n, print the nth Fibonacci number ϕn.
This problem can also be solved with a for loop.
"""
x = int(input())
lst = [1, 1]
if x == 0:
    print(0)
else:
    for i in range(0, x):
        lst.append(lst[-1] + lst[-2])
    print(lst[x-1])

""" or Better """
n = int(input())
if n == 0:
    print(0)
else:
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    print(b)

""" The index of a Fibonacci number:
Given an integer a, determine its index among the Fibonacci numbers, that is,
print the number n such that ϕn=a. If a is not a Fibonacci number, print -1
"""
import math

def fibs():
    a,b = 0,1
    yield a
    yield b
    while True:
        a,b = b,a+b
        yield b
        
def is_fib():
    fibo = 2.078087 * math.log(n) + 1.672276
    return round(fibo)
    
n = int(input())
result = is_fib()

for fib in fibs():
  if n == fib:
    print(result)
    break
  if fib > n:
    print("-1")
    break

""" or easier """
n = int(input())
if n == 0:
    print(0)
else:
    a, b = 0, 1
    n = 1
    while b <= n:
        if b == n:
            print(n)
            break
        a, b = b, a + b
        n += 1
    else:
        print(-1)

""" The maximum number of consecutive equal elements:
Given a sequence of integer numbers ending with the number 0. Determine the 
length of the widest fragment where all the elements are equal to each other 
"""
count = 1
mcount = count

while e != 0:
  e = int(input())
  if e == prev:
    count += 1
    prev = e
  else:
    if count > mcount:
      mcount = count
    count = 1
    prev = e

print(mcount)

""" or """
prev = -1
curr_len = 0
max_len = 0
e = int(input())
while e != 0:
    if prev == e:
        curr_len += 1
    else:
        prev = e
        max_len = max(max_len, curr_len)
        curr_len = 1
    e = int(input())
max_len = max(max_len, curr_len)
print(max_len)