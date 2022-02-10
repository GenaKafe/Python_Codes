x = 0

# Vesuchen: Risiko Code
try:
    x = int(input("Enter the first number: "))
    y = int(input("Enter the second number: "))

    result = x / y

except ValueError as e:
    print("[Error: 1001]",e, "\n", "Please enter a valud number between 0-9")

except ZeroDivisionError as e: 
    print("[Error: 1002]",e, "\n", "You can not devide by zero")

except Exception as  e:
    print("[Error: 1003]",e, "\n", "This is an error")

else:
    print(f" {x} / {y} = {result} ")

finally:
    print("Aufwiedersehen")

print("Ende")


'''
The try block lets you test a block of code for errors.
The except block lets you handle the error.
The finally block lets you execute code, regardless of the result of the try- and except blocks.
'''