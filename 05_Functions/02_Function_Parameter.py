
def greeting(first_name, last_name): # 2x Must Parameters
    print(f"Hallo {first_name}, {last_name}")
    print("Wie geht es dir?")
    print()

greeting("Mohamed", "Ibrahim")
greeting("Thomas", "Meier")
greeting("Sarah", "Meier")

# Achtung:
greeting(1,2) # Data types
greeting("Meier", "Thomas") # Order of the arguments
print("\n" * 5)
############################################################
# Default value
def greeting2(first_name, last_name = "***"): # 1x Must Parameter, 1x Parameter with default value
    print(f"Hallo {first_name}, {last_name}")
    print("Wie geht es dir?")
    print()

# Caller
greeting2("Ingo")
greeting2("Ingo", 'Möller')

def area(x, y="banana"):
    if y == "banana": # y: is a default value and it comes not from user
        y = x
    result = x * y
    print(f"Area {x}*{y} = {result}")

area(3,5)
area(30,5)
area(7)
area(9)
area(6,9)



"""
A function is a block of code which only runs when it is called.
You can pass data, known as parameters, into a function.
A function can return data as a result.

In Python, defining the function works as follows:
def is the keyword for defining a function. 
The function name is followed by parameter(s) in (). 
The colon : signals the start of the function body, which is marked by indentation.
"""