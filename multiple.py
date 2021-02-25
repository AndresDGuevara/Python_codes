#check if a Number is a multiple of 3. if it is, aslo check if it is a multiple of 7
print('Enter a number: ')
number = int(input())
number = 6
if number % 3 is 0:
	print('Number is a multiple of 3')
	if number % 7 is 0:
		print('Number is a multiple of 7')
	else:
		print('Number is a multiple of 3, but not multipleof 7')


