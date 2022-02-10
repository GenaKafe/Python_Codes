""" Tuples are used to store multiple items in a single variable.
(Tuple) is one of 4 built-in data types in Python used to store collections of data. 
The other 3 are List, Set, and Dictionary, all with different qualities and usage.
A tuple is a collection which is ordered and unchangeable.
"""

# Tuples are READ ONLY after declaration

teilnehmer_tuple = ("Thomas", "Ingo", "Sara", "Lena", ("A", "B"), "Jana", "Matthias")
print(teilnehmer_tuple, type(teilnehmer_tuple))


# Access Items
print(teilnehmer_tuple[0]) # Thomas
print(teilnehmer_tuple[1]) # Ingo
print(teilnehmer_tuple[-1]) # Matthias
print(teilnehmer_tuple[4]) # ('A', 'B')
print(teilnehmer_tuple[1:3]) # ('Ingo', 'Sara')
print()

# Check if item exists
if "Ingo" in teilnehmer_tuple:
    print("Ingo ist da")
print()

# Loop over tuple
for x in teilnehmer_tuple:
    print(x)
print


##############################################
# Indirect change via new declaration / creation
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
teilnehmer_tuple = ("A", "B")
print(teilnehmer_tuple, type(teilnehmer_tuple))

# 1. Create temporary list from tuple
tmp_list = list(teilnehmer_tuple)

# 2. Adjust the temp. list
tmp_list.append("C")
tmp_list.append("D")

# 3. Recreate the tuple with the new content of the .....????
teilnehmer_tuple = tuple(tmp_list)
print(teilnehmer_tuple, type(teilnehmer_tuple))


########################################
# Tuple with one single item --> needs a comma
my_tuple = ("A", "B", "C")
print(my_tuple, type(my_tuple)) # ('A', 'B', 'C') <class 'tuple'>


my_tuple = ("A")
print(my_tuple, type(my_tuple)) # A <class 'str'>


my_tuple = (50)
print(my_tuple, type(my_tuple)) # 50 <class 'int'>

# Solution: add a single comma after the single item

my_tuple = ("A", )
print(my_tuple, type(my_tuple)) # ('A',) <class 'tuple'>


my_tuple = (50,)
print(my_tuple, type(my_tuple))

