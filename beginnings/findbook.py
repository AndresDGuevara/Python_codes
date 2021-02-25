"""List and a for loop"""

collectionOfBooks = ['The Alchemist', 'How to win friends and influence poeple', 'The seven habits of highly effective people']
print('Enter the name of the book: ')
bookToBeChecked = input()
for book in collectionOfBooks:
	if book is bookToBeChecked:
		print('Yes, I do have that book!')
		break
else:
	print("I don't have that book")
	