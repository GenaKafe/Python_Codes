"""Dictionaries are used to store data values in key:value pairs.
A {dictionary} is a collection which is ordered*, changeable and does not allow duplicates.
Dictionaries have have keys and values:
"""

# Define a dictionary
#~~~~~~~~~~~~~~~~~~~~~~~~~
user = {"id": 1 , "first_name": "Thomas", "last_name": "Meier"}
print(user, type(user))

test_dic = {1 : "A", 2: "B"}
print(test_dic)
# Alternative for defining
user = dict( id=1, first_name = "Thomas", last_name = "Meier" )
print(user, type(user))

# Edit a value of a key
#~~~~~~~~~~~~~~~~~~~~~~~~~~
user["last_name"] = "Meyer"
print(user, type(user))

# Add a new key-value pair
#~~~~~~~~~~~~~~~~~~~~~~~~~~
user["car"] = True
print(user, type(user))

# If the key does not eist --> will be added, will be added, if the key exists --> will be updated

# Get a value of a key
#~~~~~~~~~~~~~~~~~~~~~~~~~
print(user.get("first_name")) # Thomas
 # print(user["first_name2"]) #  --> Error: KeyError: 'first_name2', because Key does not exist

print(user.get("first_name")) # Thomas
print(user.get("first_name2")) # Will return None --> best solution for non-existing keys
print(user.get("first_name3", "The key does not exist")) # "The key does not exist." # We can program this sentence to show up, when the key does not exist. 

# Delete a key
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
user.pop("car")
print(user, type(user))

#user.pop("first_name3") # KeyError: 'first_name3', because does not exists
user.pop("id", "banana") # returns "banana" without any error

# pop allows to delete the item and returs its value back
x = user.pop("id", "not exists") # returns "not exists" without any error
print(user, type(user))
print("x:",x)



x = user.pop("id3333", "not exists") # returns "not exists" without any error
print(user, type(user))
print("x:", x)

# Check if a key exits
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if "first_name" in user: 
    print("The key exists")
else: 
    print("The key does not exist")
print()
# Loop over Dictionary
#~~~~~~~~~~~~~~~~~~~~~~

for key in user: 
    print(key)
print()

for key in user.keys():
    print(key)
print()

for val in user.values():
    print(val)
print()

for pair in user.items(): # Tuple ('first_name', 'Thomas')
    print(pair)
print()

# Unpacking Tuple
for key,val in user.items(): # ('first_name', 'Thomas')
    print(key,val)
print()


"""
The .items() method returns a view object. 
The view object contains the key-value pairs of the dictionary, as tuples in a list.
The view object will reflect any changes done to the dictionary, see example below.
"""
