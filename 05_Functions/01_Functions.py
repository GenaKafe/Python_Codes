# Prepare (define) the functions but not call them
x = 1
def greeting1():
    print("Hallo WBS")
    print("Hallo DS")

def greeting2():
    for x in ["Thomas", "Ingo", "Sara", "Lena", "Jana", "Matthias"]:
        print(f"Hallo {x} !")
        print(f"Welches BKG {x}?")
        print(f"Warum DS {x}?")
        print()


# Call the functions
greeting1()

print()

greeting2()

print("Ende")



"""
A function is a block of code which only runs when it is called.
You can pass data, known as parameters, into a function.
A function can return data as a result.

In Python, defining the function works as follows:
def is the keyword for defining a function. 
The function name is followed by parameter(s) in (). 
The colon : signals the start of the function body, which is marked by indentation.
"""