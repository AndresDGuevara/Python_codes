introduction = """
Hello \'Friend\'! 
In this program we are going to find out who is the oldest person between two people 

Please enter your names and ages below: """

print(introduction)

a = input("\nEnter your name here: ")
age1= int(input(f'Hello {a} enter your age: '))

b = input("\nEnter second name here: ")
age2 = int(input(f"Enter {b}'s age: "))

if age1 > age2:
  print(a,'\tIs the oldest')
elif age1 is age2:
  print('Both has the same age')
else:
  print(b,'\tIs the oldest')