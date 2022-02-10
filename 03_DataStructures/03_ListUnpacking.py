# variable_name == > The rest of the list -> sublist
numbers = [1,2,3,4,5,6]

# Unpack list in variables
first = numbers [0]
second = numbers [1]
third = numbers [2]

# Alternative using Unpacking
first, second, third, *others = numbers 
print(first, second, third, others) # 1 2 3 [4, 5, 6]

#Unpacking
first, second, *others, last = numbers # [1,2,3,]
print(first, second, others, last) # 1 2 [3, 4, 5] 6


'''
When we create a list, we normally assign values to it. This is called "packing" a list.
In Python we are also allowed to extract the values back into variables. This is called "unpacking".
If the number of variables is less than the number of values, you can add an * to the variable name 
and the values will be assigned to the variable as a list.
'''

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green) # apple
print(yellow) # banana
print(red) # ['cherry', 'strawberry', 'raspberry']