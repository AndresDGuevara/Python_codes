# import random
# import string

# letters = string.ascii_letters
# nums = '0123456789'
# spe = '""/*-+!#$%&/()?¡¿{}[]-_|°@<>='
# symbols = letters + nums + spe

# len = int(input("Enter Password Lenght: "))
# password = "".join(random.sample(symbols, len))

# print("Your New Password is: ", password)   



# import random
# from string import digits, punctuation, ascii_letters

# symbols = ascii_letters + digits + punctuation
# secure_random = random.SystemRandom()

# len = (int(input("Enter password length: ")))
# password = "".join(secure_random.choice(symbols) for a in range (len))

# print("Your new password is: ", password)


import random
from string import digits, punctuation, ascii_letters

def password_generator():

    symbols = ascii_letters + digits + punctuation
    password = []
        
    len = (int(input("Enter password length: ")))

    for a in range (len):
        secure_random = random.choice(symbols)
        password.append(secure_random)

    password = "".join(password)
    return password    


def run():
    password = password_generator()
    print("Your new password is: ", password)


if __name__ == '__main__':
    run()