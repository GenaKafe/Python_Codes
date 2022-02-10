glass = 0.08
plastic = 0.25

print("Anzahl von den Glassflaschen ")
number_glass = int(input())

print("Anzahl von den Plastikflaschen ")
number_plastic = int(input())

print("Ihr Guthaben beträgt: " + str(number_glass * glass + number_plastic * plastic))
