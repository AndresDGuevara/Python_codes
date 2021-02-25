def square (x):
	return x * x

square(25)
625
square(5)
25

def even_or_odd(n):
	if n % 2 == 0:
		print("even")
		return
	print("odd")

	
w = even_or_odd(31)
#odd
w is None
True

def nth_root(radicand, n):
	return radicand ** (1/n)

nth_root(16, 3)
2.5198420997897464

nth_root(16, 2)
4.0

def display_nth_root(radicand, ordinal, n):
	root = nth_root(radicand, ordinal, n)
	message = 'The' + ordinal(n) + 'root of' + str(radicand) + 'is' + str(root)
	print(message)