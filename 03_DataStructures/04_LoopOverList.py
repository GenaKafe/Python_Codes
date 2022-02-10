# We can loop through (over) the list items by using a for loop.

teilnehmerliste = ["Thomas", "Ingo", "Sara", "Lena", "Jana", "Matthias"]

counter = 1
for teilnehmer in teilnehmerliste:
    print(f"{counter}." , teilnehmer)
    counter += 1
print("\n\n")
########################################
user_data = ["Mattias", "Möller", 55, 37.2, True, ["Jana", "Sara"]]

for x in user_data: 
    print(x, type(x))


print("\n\n")
########################################
# enumerate() --> BG "izbrojavam, izrejdam" / DE "etw. aufzählen"
# returns a tuple (index, value)
"""
The enumerate() function takes a collection (e.g. a tuple) and returns it as an enumerate object.
The enumerate() function adds a counter as the key of the enumerate object.
"""

teilnehmerliste = ["Thomas", "Ingo", "Sara", "Lena", "Jana", "Matthias"]

for teilnehmer in enumerate(teilnehmerliste): # tuple (0, 'Thomas')
    print(teilnehmer) # (0, 'Thomas'), (1, 'Ingo')
    print(f"Index: {teilnehmer[0]} - Value: {teilnehmer[1]}") # Index: 0 - Value: Thomas
    print()

# enumerate combined with unpacking
for idx, val in enumerate(teilnehmerliste): # tuple (0, 'Thomas')
    print(f"Index: {idx} - Value: {val}")


