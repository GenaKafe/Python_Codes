odd_number_list = ""
sum_odd_numbers = 0
count_odd_numbers = 0

lower_limit = int(input("Bitte die Untergrenze eintippen: "))
upper_limit = int(input("Bitte die Obergrenze eintippen: "))

lower_limit < upper_limit == True # FIXME: what do I want to achieve?


for x in range(lower_limit, upper_limit+1): # [1,2,3,4,5,6,7,8,9]
    if x%2 == 1: # ungerade
        odd_number_list += str(x) + ", "
        sum_odd_numbers += x
        count_odd_numbers += 1

print(f"All odd numbers between {lower_limit} und {upper_limit}:")
print(f"All odd numbers: {odd_number_list}")
print(f"Summ odd numbers: {sum_odd_numbers}")
print(f"Count odd numbers: {count_odd_numbers}")