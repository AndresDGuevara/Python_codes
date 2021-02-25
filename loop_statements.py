>>> number = 1
>>> for row in range(1, 4):
	for column in range(1, 4):
		print(number, end = '')
		number = number + 1
	print()
123
456
789

>>> for number in range(1, 10):
	if number is 5:
		break
	else:
		print(number)
1
2
3
4

>>> for number in range(1, 10):
	if number is 5:
		continue
	else:
		print(number)
1
2
3
4
6
7
8
9
>>> 
>>> for number in range(1, 11):
	if number is 15:
		break
	else:
		print(number)
else:
	print('All the numbers were printed without breaking the loop')

1
2
3
4
5
6
7
8
9
10
All the numbers were printed without breaking the loop

>>> for number in range(1, 11):
	if number is 5:
		break
	else:
		print(number)
	else:
		print('All the numbers were printed without breaking the loop')
1
2
3
4
>>> 