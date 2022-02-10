# Übung 6A Ungerade Zahlen
print("\n")

user_input = ""
odd_numbers = ""
odd_list = ""
# num = ""
# odd_list = ""

total_odd = 0

user_input = int(input("Bitte eine ganze Zahl eintippen: "))

for num in range(1, user_input,2):
    odd_numbers += str(num) + ", "
    total_odd += 1

""" # correct but once I am done with the rest
    if num == user_input:
        print()
"""

"""
    if num == odd_numbers:
    total_odd = int(len(num) # IndentationError: expected an indented block
"""
  

"""
for num in range(1, user_input,2):
    odd_numbers += str(num) + ", "
    odd_list = [odd_numbers]
    total_odd += num(odd_list) # TypeError: 'int' object is not callable
"""

"""
for num in range(1, user_input,2):
    odd_numbers += str(num) + ", "
    total_odd += num(odd_numbers)
"""

print("Die ungeraden Zahlen sind: ", odd_numbers)
print("Insgesamt: ", total_odd) # that is sum! (not number)

#print("Insgesamt: ", len(odd_numbers)) gives me the number of symbols