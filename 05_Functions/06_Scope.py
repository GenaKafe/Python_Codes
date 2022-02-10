location = "Berlin"

# Read global variable from local scope
def greeting(first_name, last_name):
    print(location) # Read Only global variable
    print("Hello", first_name, last_name)

greeting("Thomas", "Meier")
location = "Hamburg"
greeting("Ingo", "Meier")
################################################

def greeting2(first_name, last_name):
    location = "Aachen" # creates a new local variable (not change the global variable)
    print(location) # Aachen
    print("Hello", first_name, last_name)


greeting2("Sara", "Meier")
print(location) # Hamburg

###############################################

def greeting3(first_name, last_name):
    global location # makes the global variable -> editable
    location = "Frankfurt" #
    print(location) #
    print("Hello", first_name, last_name)

 
greeting3("Lena", "Meier")
print(location) # Frankfurt

""" A variable is only available from inside the region it is created. This is called scope.
A variable created inside a function belongs to the local scope of that function, 
and can only be used inside that function.
"""

'''
In Python, the concept of scope is closely related to the concept of the namespace.
As you've learned so far, a Python scope determines where in your program a name is visible. 
Python scopes are implemented as dictionaries that map names to objects. 
These dictionaries are commonly called namespaces.
'''




