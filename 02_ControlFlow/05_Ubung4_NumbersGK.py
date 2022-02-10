num_list = [3,9,13,19,23,-4,-10,-14,-20,-24]

print("Alle Zahlen:")
for num in num_list:
    print(num, end = " ")
    if num == 10:
        print()
print('\n')

print("Alle positiven Zahlen:")
for num in num_list:
    if num >= 0:
        print(num, end = " ")
print('\n')

print("Alle negativen Zahlen:")
for num in num_list:
    if num < 0:
        print(num, end = " ")
print('\n')

print("Summe von allen Zahlen:")
sum_all = sum(num_list, 0)
print(sum_all)




