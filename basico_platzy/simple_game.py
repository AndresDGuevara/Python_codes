import random

def run():
    aleatory_num = random.randint(1, 20)
    lives = 4
    tries = 1
    user_num = int(input("""Choose one number from 1 to 10 You have 4 tries -->"""))

    while user_num != aleatory_num:
        lives -= 1 #every loop, it susbtracts one life
        tries += 1 #every loop, it adds one try
        if user_num < 1 or user_num > 10 or lives == 0:
            print("---/// You lost ///---")
            print("The aleatory number was", aleatory_num)
            break
        elif user_num < aleatory_num:
            print("Look for a 'higher' number")
        elif user_num > aleatory_num:
            print("Look for a 'lower' number")
        print("You have", lives, "lives remaining: ")
        user_num = int(input("Choose another number: "))
    if user_num == aleatory_num:
        print("--> YOU WON <-- With", tries, "tries." )


if __name__ == '__main__':
    run()