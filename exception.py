#this code is to take control of the errors the terminal can throw at us when we do not use the right names or numbers. with this try and except block we can handle those error and make themm look good
try:
    length = 10
    width = 0
    length / width
except Exception:
    print("Division by zero is invalid! Kindly change your input")

except NameError:
    print("Variable has been used before defining it")

except ZeroDivisionError:
    print("Division by zero is invalid! Kindly change your input")
