"""
20.10.2021  
Fizz Buzz 
The function has a number that comes from the user (input). 
This number / 3 --> then my system should print Fizz
This number / 5 -->  
 / 3 and 5 --> FuzzBuzz
Otherwise we write the number(input) that is given to us.
"""
########################################################
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Welcome to the game Buzz Fuzz")
print() 

# user_number = int(input("Please enter a number: "))

def fizz_buzz(user_number):
    if (user_number %3 == 0) and (user_number %5 == 0):
        return "Fizz Buzz"
    if user_number %3 == 0:
        return "Fizz"
    if user_number %5 == 0:
        return "Buzz"
    return user_number

# print(fizz_buzz(f" Result: {user_number}"))

print(fizz_buzz(15))

        






