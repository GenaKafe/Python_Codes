# SET
#~~~~~~~~~~~~~~~~
"""
1. Whiout Duplication
2. Has no index (un-indexed) -> print(numbers[0]) : error
3. Order is different
"""
numbers_set = {1,1,1,2,3,4,5,6} # SET
print(numbers_set, type(numbers_set)) # {1, 2, 3, 4, 5, 6} <class 'set'>

# Add new items
numbers_set.add(7)
numbers_set.add(8)
print(numbers_set)

# Add several items
numbers_set.update([9,10,11,12])
print(numbers_set)

# len()
print(len(numbers_set)) # 12

# Create a set from list
my_number_list = [100,100,100,120,130,11,12]
my_number_set = set(my_number_list)
print(my_number_list) # {130, 100, 11, 12, 120}

# combine two sets
combined_set = numbers_set.union(my_number_list)
print(combined_set) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 100, 130, 120}


# common items in both sets
print(my_number_set & numbers_set) # {11, 12}

# print only the first set items
print(my_number_set - numbers_set)  # {120, 130, 100}

# print all items except the common one
print(my_number_set ^ numbers_set) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100, 130, 120}