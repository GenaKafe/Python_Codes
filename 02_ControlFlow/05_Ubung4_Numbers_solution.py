all_numbers = ""
positive_numbers = ""
negative_numbers = ""

sum_all = 0
sum_positive = 0
sum_negative = 0

# The user enters with how many loops (input numbers) would like to have. 
count_loops = int(input("Enter the number of loops: "))

for x in range(count_loops): # 10x loops
    user_number = int(input("Enter number: >"))
    all_numbers += str(user_number) + ", "
    sum_all += user_number

    if user_number >=0:   # positive numbers
        positive_numbers += str(user_number) + ", "
        sum_positive += user_number

    else: # negative numbers
        negative_numbers += str(user_number) + ", "
        sum_negative += user_number

# Output
print("All numbers are: ", all_numbers)
print("POS numbers are: ", positive_numbers)
print("NEG numbers are: ", negative_numbers)

print("Sum of all numbers: ", sum_all)
print("Sum of positive numbers: ", sum_positive)
print("Sum of negative numbers: ", sum_negative)