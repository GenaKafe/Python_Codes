x = 0
try:

    x = int(input("Enter a positive number: "))

    if x<0:
        raise ValueError("Your input is not a positive number!") # manuel error

except ValueError as e:
    print(e) # Your input is not a positive number!

else: 
    print("x: ",x)

print("Ende")

"""As a Python developer you can choose to throw an exception if a condition occurs.
To throw (or raise) an exception, use the raise keyword.
The raise keyword is used to raise an exception.
You can define what kind of error to raise, and the text to print to the user.
"""