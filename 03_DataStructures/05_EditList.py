teilnehmerliste = [] # empty list

teilnehmerliste = ["Thomas", "Ingo", "Sara", "Lena", "Jana", "Mathias"]
print(teilnehmerliste)

# List methods:
#~~~~~~~~~~~~~~~~~~

# Add
#~~~~~~~~~~~~~~~~~~
teilnehmerliste.append("Frank") # add the item to the end fo the list
print(teilnehmerliste)

teilnehmerliste.insert(2, "Sven") # add the item to a specific position
print(teilnehmerliste)


# Edit Values: 
#~~~~~~~~~~~~~~~~~~~~~~~~
teilnehmerliste[0] = "Liane"
print(teilnehmerliste)


# Delete
#~~~~~~~~~~~~~~~~~~~~
teilnehmerliste.pop() # deletes the last item
print(teilnehmerliste)

teilnehmerliste.pop(1) # deletes a specific index
print(teilnehmerliste)

teilnehmerliste.remove("Jana") # deletes the first match
print(teilnehmerliste)

# Alternative (special function)
del teilnehmerliste[1] # deletes "Sven"
print(teilnehmerliste)


del teilnehmerliste[0:2]
print(teilnehmerliste)




 