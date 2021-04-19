""" a tuple with two items that are both lists. 
first one holds a list of even numbers up to 10.0 
The second holds the odd numbers up to 20
"""

mytuple = ([i for i in range (10) if i % 2 == 0], [j for j in range(20) if j % 2 != 0])
print(mytuple)