# 0. Phase: Annehmen


# 1. Phase: User inputs

# user_count_numbers = int(input("Please enter the count of the numbers: "))


iteration_count = int(input("Enter a positive number: ")) # break - when the function to stop

# 2. Phase: Calculation
result = []


def addieren(x,y):
    result = x + y
    return result
    # For iteration 2 find index 2 from the list above 
    # repeat as many times as in input

# 3. Phase. Print result
 
addieren(0,1)
print(f"{1} + {result} = {result}")
addieren(1,1)
print(f"{1} + {result} = {result}")


# formula1: 0+1=1 (0,1,result) # result = index(1 + 2)
# formula2: 1+result=result index(1,2,result) # result = index(1 + 2)
# repeat formula 2 by input times


