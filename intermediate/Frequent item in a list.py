# Find the most frequent item in a list (of integers here)

data = [10, 20, 30, 10, 20, 40, 20]
# the answer is 20

# 1. Convert the list to a set
# 2. Find the max using the key
# where the key is the number of items.
# 3. print

print(max(set(data), key = data.count))

# First you convert the list to a set. In the set, you will not have repeating items. In other words,
# you get a list of all unique items in the list. Then find the max using the build-in 'max' function but 
# with a small addition: 'key = data.count' it will use the value for sorting the items. So, for example
# 'data.count(30)' retunrs 1 and data.count(20) returns 3, and those two numbers are compared in the end
# instead of comparing 10 and 20
 