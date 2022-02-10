
print("Willkommen bei Lidl")
print("~~~~~~~~~~~~~~~~~~~~")


# 0. Phase : Annahmen / Configuration / Einstellungen
GLASS_PRICE = 0.08
PLASTIC_PRICE = 0.25
CURRENCY = "EURO"


# 1. Phase: User Inputs
count_glass = int(input("Anzahl von Glassflaschen:  "))
count_plastic = int(input("Anzahl von Plastikflaschen:  "))

# 2. Phase: Calculation 
result = count_glass * GLASS_PRICE + count_plastic * PLASTIC_PRICE


# 3. Print Results
print("Ihr Guthaben beträgt:", result, CURRENCY)