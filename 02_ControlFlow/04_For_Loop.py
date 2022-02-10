for teilnehmer in ['Thomas', 'Ingo', 'Sara']:
    print("Welcome:", teilnehmer)
    print("~" * 20)
    print("What is your name:", teilnehmer)
    print("Which Background?")
    print("Why DS?")
    
print()

for x in [1,2,3,4,5,6]:
    print(x)

print("~" * 20)

for x in [1,2,3,4,5,6]:
    print(x, end = " ")
    if x == 6:
        print()

print("Python")

print("+" * 20)

"""
for x in [1,2,3,5,6]:
    user_input = input("Enter your wish?")
    print("Ihr Wunsch ist:", user_input)
"""

######################################
# range(): generates numbers

# range(10): 0-9 [0,1,2,3,4,....,9]
for num in range(10):
    print(num)
print()

# range(5,10) : 5-9 [5,6,7,8,9]
for num in range(5,10):
    print(num)
print()

# range(1,20,2): [1,3,5,7,19]
for num in range(1,20,2):
    print(num)