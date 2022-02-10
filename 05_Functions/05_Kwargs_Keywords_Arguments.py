#  **: Kwargs --> KeyWord Arguments --> dictionary of (key, value)
#  When I don't know how many keyword arguments will be passed into the function and
#  the caller sends us the paramaters.

def greeting(**container):
    print(container)

    for key, val in container.items():
        print(f"Key:{key} Value:{val}")
        print()

    if "car" in container: 
        print("Car key is avalable: ", container.get("car"))
    else:
        print("Car key does not exists.")


# Caller
greeting(first_name = "Mohamed", last_name = "Ibrahim") # {'first_name': 'Mohamed', 'last_name': 'Ibrahim'}
greeting(id=1, first_name = "Thomas", car = True) # {'id': 1, 'first_name': 'Thomas', 'car': True}

"""
A keyword argument is where you provide a name to the variable as you pass it into the function.
One can think of the kwargs as being a dictionary that maps each keyword to the value that we pass alongside it. 
That is why when we iterate over the kwargs there doesn't seem to be any order in which they were printed out.
The special syntax **kwargs in function definitions in python is used to pass a keyworded, variable-length argument list. 
We use the name kwargs with the double star. 
The reason is because the double star allows us to pass through keyword arguments (and any number of them).

"""