""" Given two integers A and B. Print all numbers from A to B inclusively, 
 in ascending order, if A < B, or in descending order, if A ≥ B. 
"""

a = int(input("First Integer: "))
b = int(input("Second Integer: "))
if (a < b):
    print("The numbers in ascending order are:")
    for i in range(a, b + 1):
        print(i)
else:
    print("The numbers in descending order are:")
    for i in range(a, b - 1, -1):
        print(i)