
odd_number_list = ""
sum_odd_numbers = 0
count_odd_numbers = 0

lower_limit = int(input("Enter the lower limit: ")) # 1
upper_limit = int(input("Enter the upper limit: ")) # 9


for x in range(lower_limit, upper_limit+1): # [1,2,3,4,5,6,7,8,9]
    if x%2 == 1: # ungerade
        odd_number_list += str(x) + ", "
        sum_odd_numbers += x
        count_odd_numbers += 1


average_odd_numbers = sum_odd_numbers / count_odd_numbers

print(f"All odd numbers between {lower_limit} and {upper_limit}:")
print(f"All odd numbers: {odd_number_list}")
print(f"Summ odd numbers: {sum_odd_numbers}")
print(f"Count odd numbers: {count_odd_numbers}")
print(f"Average odd numbers: {average_odd_numbers}")