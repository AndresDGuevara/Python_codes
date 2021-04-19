# Still working on it
def draw_cards(num):
  choose_red(num)
  if num < 8:
    print(num)
  else:
     choose_black(num)

def choose_red(num):
  print(num, 'of hearts')
  if num > 4:
    print(num)
  else:
    print(num, 'of diamonds')

def choose_black(num):
  if num > 10:
    print(num, 'of clubs')
  else:
    print(num, 'of spades')

def run():
  print("\n\tWelcome to 5 of hearts\n")
  
  num = int(input("\tEnter a number: "))
  while True:
    menu = """ Choose one of the options below
    1- Draw Cards
    2- Choose Red
    3- Choose Black
    4- Quit the game
    Choose one of the options: 
    """
    try:
      option = int(input(menu))
    except ValueError:
      print("Wrong choice!, try again")
      continue

    if option == 1:
      draw_cards(num)
    elif option == 2:
      choose_red(num)
    elif option == 3:
      choose_black(num)
    elif option == 4:
      print("Thanks for playing")
      break

if __name__ == '__main__':
  run()
  