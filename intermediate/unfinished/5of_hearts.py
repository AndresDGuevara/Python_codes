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