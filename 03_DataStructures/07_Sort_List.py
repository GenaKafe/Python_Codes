numbers = [13,4,5,7,2,6,2,6,8,45,23]
print(numbers)


# 1. Variant: List Method: changes the orginal list
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
numbers.sort() # ascending = aufsteigend
print(numbers)

numbers.sort(reverse=True) # descending = absteigend
print(numbers)
print()

##################################
# 2. Variant: it creates a new sorted list
numbers = [13,4,5,7,2,6,2,6,8,45,23]

sorted_list = sorted(numbers) # aufsteigend
print(sorted_list)


sorted_list = sorted(numbers, reverse=True)
print(sorted_list)
