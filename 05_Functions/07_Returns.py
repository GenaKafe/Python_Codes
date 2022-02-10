
# without return
def addieren_1(x,y):
    result = x + y
    print("Result:", result)

# With return
def addieren_2(x,y):
    result = x + y
    return result

# Multiple returns
def addieren_3(x,y):
    result = x + y
    return result, "Das Ergebnis beträgt", True


# Caller
addieren_1(3,6)

# Single Return
total = addieren_2(50,60)
print("The result of two number is: ", total)

# Multiple Returns
total, message, status = addieren_3(200,300)
print(total, message, status)


"""
The Python return statement is a key component of functions and methods. 
You can use the return statement to make your functions send Python objects back to the caller code. 
These objects are known as the function’s return value. 
You can use them to perform further computation in your programs.
Using the return statement effectively is a core skill if you want to code custom functions that are Pythonic and robust.

"""