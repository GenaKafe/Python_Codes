teilnehmerliste = ["Thomas", "Ingo", "Sara", "Lena", "Jana", "Matthias"]

if "Thomas" in teilnehmerliste:
    print("Der Teilnehmer ist schon da.")
else: 
    print("Der Teilnehmer ist nicht da.")


if "Someone" not in teilnehmerliste:
    print("Someone does not exist.")
else: 
    print("Someone eixsts.")


########################################################
# Find the index of a value: 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

print(teilnehmerliste.index("Sara")) # 2
# print(teilnehmerliste.index("Banana")) # Error > Banana does not exist

if ("Banana") in teilnehmerliste: # False
    print(teilnehmerliste.index("Banana"))
else:
    print("Banana ist nicht da")