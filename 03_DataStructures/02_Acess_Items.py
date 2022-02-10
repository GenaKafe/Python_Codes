teilnehmerliste = ["Thomas", "Ingo", "Sara", "Lena", "Jana", "Mathias"]

print(teilnehmerliste[0])
print(teilnehmerliste[1])
print(teilnehmerliste[-1])
print(teilnehmerliste[0:4])
print(teilnehmerliste[0:6:2]) # Jump by 2 ['Thomas','Sara']
print(teilnehmerliste[0::2]) # Jump by 2 ['Thomas','Sara']
print(teilnehmerliste[::2]) # Jump by 2 ['Thomas','Sara']
print(teilnehmerliste[::3]) # Jump by 3 ['Thomas, 'Lena']

print()

############################
# Access Sub list items: 
#~~~~~~~~~~~~~~~~~~~~~~
user_data = ["Thomas", "Meier", ["A", "B", "C"], True]

print(user_data[1]) # Meier
print(user_data[2]) # ['A', 'B', 'C']

print('~' * 20)

# create the sub list
x = user_data[2] # ['A', 'B', 'C']
print(x)

# find the item: 1 form the sublist
print(x[1]) # B

# Alternative: Acces sub list directly
print(user_data[2][1])

user_data = ["Thomas", "Meier", ["A", "B", "C"] , ["AA", "BB", ["CC", "DD"]]]

print(user_data[3][0]) # AA

print(user_data[3][2][1]) # DD