# Ideal Fall
print("\n")

age = 19
payment_method = False
items = 0
customer_card = True

message = ""

if (age >= 18) and (payment_method == True) and (items > 0) and (customer_card == True):
    message = "Sie dürfen zur Kasse!"
else:
    if age < 18:
        message += "Sie sind zu jung!\n"

    if payment_method == False:
        message += "Sie müssen Bezahlungsmethode eingeben!\n"
    
    if items < 1:
        message += "Sie benötigen Produkte bevor Kasse!\n"
    
    if customer_card == False:
        message += "Sie brauchen eine Kundenkarte!\n"

print(message)
