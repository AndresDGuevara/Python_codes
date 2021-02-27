"""Given three integers, print the smallets value: """
def smallestNumber(a, b, c):
    
    if a < b and a < c:
        print('First integer is the smallets')
        return a
    elif b < c:
        print('Second integer is the smallest')
        return b
    else:
        print('Third integer is the smallest')
        return c

print('Enter three integers numbers below: ')
a = int(input("First Integer: "))
b = int(input("Second Integer: "))
c = int(input("Third Integer: "))

smallestNumber = smallestNumber(a, b, c)    
print(f'The smallest Number of the list is {smallestNumber}'.format(smallestNumber))