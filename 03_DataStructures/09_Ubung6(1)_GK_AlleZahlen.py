
# 0 Phase: Annehmen
user_list = []
positive_numbers = []
negative_numbers = []
sum_all = 0    


# 1 Phase: User inputs - user inputs numbers until 0 (exit point)


"""
for number in user_list !=0:
    number = 
"""
# 2. Phase: Calculation

while True:
    user_input = int(input("Please enter a whole number: "))
    if user_input == 0:
        break
    user_list.append(user_input)
    sum_all += user_input
    if user_input > 0:   # positive numbers
        positive_numbers.append(user_input)
    else: # negative numbers
        negative_numbers += str(user_input) + ", " # FIXME: correction to a list


# Sort the list # FIXME: in place
sorted_list = sorted(user_list)
sorted_list_pos = sorted(positive_numbers)
sorted_list_neg = sorted(negative_numbers)

# print("Tippe 0 zum Abbrechen mit der Numbereingabe ein.")


# 3. Phase: Output
print(f"Alle Zahlen sind: {user_list}")
print(f"Alle positiven Zahlen sind: {positive_numbers}:")
print(f"Alle negativen Zahlen sind: {negative_numbers}:")
print(f"Summe aller Zahlen: ",sum(user_list))
print(f"Minimum Zahl: ", min(user_list))
print(f"Maximumal Zahl: ", max(user_list))