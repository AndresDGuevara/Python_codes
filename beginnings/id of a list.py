fruits = ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']

id(fruits)
12964728

id(fruits.sort())
1825799236
# the id is different, calling the sort funciont in python on a list results in a different or new object,
#  which has a different allocation in memory, but python keeps the name from the old one. so it's just 
# pointing to a different location
