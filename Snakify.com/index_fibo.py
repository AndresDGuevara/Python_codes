import math
n = int(input('enter number: '))

def findIndex(n):
    fibo = 2.078087 * math.log(n) + 1.672276
    return round(fibo)
    
result = findIndex(n)
print(findIndex(n))

# import math

# x = int(input())

# phi = 1.61803399
# sqrt5 = math.sqrt(5)

# def F(n):
#   return int((phi**n - (1-phi)**n) / sqrt5)
    
# def isFibonacci(z):
#   return F(int(math.floor(math.log(sqrt5 * z,phi) + 0.5))) == z

# if isFibonacci(x) == True:
#   print(round(math.log(x * sqrt5 + 0.5) / math.log(phi)))
# else:
#   print(-1)



# n = int(input())
# a, b = 0, 1
# for index in range(2, n + 1):
#     a , b = b, a + b
# print(a)
 

# import math
# n = int(input())
# print(math.log(n*math.sqrt(5)+0.5)/math.log(1.61803398875)-1)
	    

# def findIndex(n):
#     a = 0
#     b = 1
#     c = 1
#     res = 1
    
#     while (c < n):
#         c = a + b
#         res = res + 1
#         a = b
#         b = c
#     return res

# n = int(input())
# result = findIndex(n)
# if findIndex == True:
#     print(result)
# else:
#     print('-1')

# import math
# n = int(input())

# def findIndex(n):
#     fibo = 2.078087 * math.log(n) + 1.672276
#     return round(fibo)
    
# if findIndex == True:
#     print(findIndex(n))
# else:
#     print('-1')
    



    

