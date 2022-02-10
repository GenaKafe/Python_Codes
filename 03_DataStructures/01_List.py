"""" Lists are used to store multiple items in a single variable.
[Lists] are one of 4 built-in data types in Python used to store collections of data.
The other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
List items are ordered, changeable, and allow duplicate values.
List items are indexed, the first item has index [0], the second item has index [1] etc.
When we create a list, we normally assign values to it. This is called "packing" a list.
In Python we are also allowed to extract the values back into variables. This is called "unpacking".
"""
letters = ['a', 'b', 'c', 'd'] # 'a' = "a"
print(letters , type(letters)) # ['a', 'b', 'c', 'd'] <class 'list'>

numbers = [1, 2, 3, 4, 5, 6, 7]
print(numbers)

# combine two different lists
combined = letters + numbers
print(combined) # ['a', 'b', 'c', 'd', 1, 2, 3, 4, 5, 6, 7]

# Vector
zeros = [0] * 20
print(zeros)

# Matrix
matrix = [ [0,1] , [2,3]]
print(matrix)

# Conversion function list ()
###############################

x = list(range(5,9))   # [5, 6, 7, 8]
print(x)

chars = list("Python programierung")
print(chars)