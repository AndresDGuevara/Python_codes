"""number divisible by 10, 50, 30"""
number = 150
if number % 10 == 0 and number % 50 == 0:
    if number % 30 == 0:
        print('This number is divisible by 10, 50 and 30')
    else:
        print('This number is divisible by 10 and 50 but not 30')
n = int(input('Numeros'))
