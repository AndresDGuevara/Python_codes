"""Slices:
You are given a string.
1) In the first line, print the third character of this string.

2) In the second line, print the second to last character of this string.

3) In the third line, print the first five characters of this string.

4) In the fourth line, print all but the last two characters of this string.

5) In the fifth line, print all the characters of this string with even indices 
(remember indexing starts at 0, so the characters are displayed starting with the first).

6) In the sixth line, print all the characters of this string with odd indices 
(i.e. starting with the second character in the string).

7) In the seventh line, print all the characters of the string in reverse order.

8) In the eighth line, print every second character of the string in reverse order, 
starting from the last one.

9) In the ninth line, print the length of the given string.
"""
s = input()
print(s[2]) # 1
print(s[-2]) # 2
print(s[:5]) # 3
print(s[:-2]) # 4
print(s[::2]) # 5
print(s[1::2]) # 6
print(s[::-1]) # 7
print(s[::-2]) # 8
print(len(s)) # 9

""" The number of words:
Given a string consisting of words separated by spaces. Determine how many words it has. 
To solve the problem, use the method count.
"""
s = input()
print(len(s.split()) )

""" or """
print(input().count(' ') + 1)

""" The two halves:
Given a string. Cut it into two "equal" parts (If the length of the string is odd, 
place the center character in the first string, so that the first string contains 
one more characther than the second). Now print a new string on a single row with 
the first and second halfs interchanged (second half first and the first half second)
Don't use the statement if in this task.
"""
from math import ceil

lst = list(str(input()))
h = ceil(len(lst) / 2)
r = lst[h:] + lst[:h]
print(''.join(r))

""" or """
s = input()
print(s[(len(s) + 1) // 2:] + s[:(len(s) + 1) // 2])

""" To swap the two words:
Given a string consisting of exactly two words separated by a space. Print a new string 
with the first and second word positions swapped (the second word is printed first).
This task should not use loops and if.
"""
s = input()
w = s.split()
w = list(reversed(w))
print(" ".join(w))

""" or """
s = input()
first_word = s[:s.find(' ')]
second_word = s[s.find(' ') + 1:]
print(second_word + ' ' + first_word)

""" The first and last occurrence:
Given a string that may or may not contain a letter of interest. Print the index location 
of the first and last appearance of f. If the letter f occurs only once, then output its index. 
If the letter f does not occur, then do not print anything.
Don't use loops in this task.
"""
s = input()
if s.count("f") >= 2:
  print(s.find("f"), s.rfind("f"))
elif s.count("f")== 1:
    print(s.find("f"))
else:
    None

""" or better """
s = input()
if s.count('f') == 1:
    print(s.find('f'))
elif s.count('f') >= 2:
    print(s.find('f'), s.rfind('f'))

""" The second occurrence:
Given a string that may or may not contain the letter of interest. Print the index location 
of the second occurrence of the letter f. If the string contains the letter f only once, 
then print -1, and if the string does not contain the letter f, then print -2.
"""
s = input()

if s.count("f") >= 2:
  print(s.find("f", s.find("f") + 1))
elif s.count("f") >= 1:
  print('-1')
else:
  print(-2)

""" or better """
s = input()
if s.count('f') == 1:
    print(-1)
elif s.count('f') < 1:
    print(-2)
else:
    print(s.find('f', s.find('f') + 1))

""" Remove the fragment:
Given a string in which the letter h occurs at least twice. Remove from that string the first 
and the last occurrence of the letter h, as well as all the characters between them.
"""
t = input()
if t.count("h") >= 2:
  print(t[:t.find("h")] + t[t.rfind("h") + 1:])
else:
  print(t.count("h"))

""" or better """
s = input()
s = s[:s.find('h')] + s[s.rfind('h') + 1:]
print(s)

"""Reverse the fragment:
Given a string in which the letter h occurs at least two times, reverse the sequence of 
characters enclosed between the first and last appearances.
"""
s = input()
a = s[:s.find("h") + 1]
b = s[s.rfind("h"):]
c = s[s.find("h") + 1:s.rfind("h")]

if s.count("h") >= 2:
  print(a + c[::-1] + b)
else:
  print(s.count("h"))

""" or better """
s = input()
a = s[:s.find('h')] 
b = s[s.find('h'):s.rfind('h') + 1]
c = s[s.rfind('h') + 1:]
s = a + b[::-1] + c
print(s)

""" Replace the substring:
Given a string. Replace in this string all the numbers 1 by the word one.
"""
s = input()
print(s.replace('1', 'one'))

""" or better """
print(input().replace('1', 'one'))

""" Delete a character:
Given a string. Remove from this string all the characters @.
"""
s = input()
print(s.replace('@', ''))

""" or better """
print(input().replace('@', ''))

""" Replace within the fragment:
Given a string. Replace every occurrence of the letter h by the letter H, except for the first and the last ones.
"""
s = str(input())
slice = s[s.find("h") + 1:s.rfind("h")]
print(s[:s.find("h") + 1] + slice.replace("h","H") + s[s.rfind("h"):])

""" or better """
s = str(input())
a = s[:s.find("h") + 1]
b = s[s.find("h") + 1:s.rfind("h")]
c = s[s.rfind("h"):] 
s = a + b.replace("h","H") + c
print(s)

""" Delete every third character:
Given a string. Delete from it all the characters whose indices are divisible by 3.
"""
s = input()
t = ""
for i in range(len(s)):
  if i % 3 != 0:
    t += s[i]
print(t)

""" 
"""
