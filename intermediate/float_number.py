"""
Given a positive real number, print its first digit to 
the right of the decimal point.

Example input
1.79

Example output
7
"""

a = float(input("Enter a floating number:")) # Get the input from user as a float number

import math #using the math module function

frac=math.modf(a) # 1. 

frac1=str(frac[0]) # 2. 

print("1st digit after the decimal point is:", frac1[2]) # 3. 

# 1. Using "modf(x)" function we are getting the fraction and integer part as a tuple
#    of fraction part in index 0 and integer part in index1.

# 2. As our o\p needs to produce the decimal alone so we are 
#    converting the fraction tuple alone in to a string 

# 3. As our o\p needs to print the value after the decimal point,
#    we are printing the 2nd index position of the fractional string
