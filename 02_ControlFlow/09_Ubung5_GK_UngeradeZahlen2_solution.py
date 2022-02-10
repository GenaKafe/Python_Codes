odd_numbers = ""

total_odd = 0

lower_limit = int(input("Bitte eine niedrige Zahl eintippen: "))
upper_limit = int(input("Bitte eine höchere Zahl eintippen: "))
# range_odd = range(lower_limit, upper_limit, 2)
print(f"Danke, Ihre ausgewählten Zahlen sind: {lower_limit} and {upper_limit}")
print("\n")

"""
for num in range(range_odd):
    odd_numbers = str(num) + ", " # TypeError: 'range' object cannot be interpreted as an integer
    #total_odd += sum(odd_numbers)
"""


for num in range(1, upper_limit + 1, 2): # range start
    odd_numbers += str(num) + ", "
    
    if num == upper_limit:
        print()
        break
    #total_odd += sum(odd_numbers)

# Outputs     
print("Die ungeraden Zahlen sind: ", odd_numbers)
#print("Die Summe davon ist: ", total_odd)





