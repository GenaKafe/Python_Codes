# Online Shopping 1

age = 18
payment_method = False


if (age >=18) and (payment_method == True):
    print("Sie dürfen zur Kasse!")
elif (age < 18) and (payment_method == True):
    print("Sie sind zu jung")
elif (age >= 18) and (payment_method == False):
    print("Sie müssen Bezahlungsmethode eingeben.")
elif (age < 18) and (payment_method == False):
    print("Sie sind zu jung UND Sie Müssen Bezahlungsmethode eingeben!")

#################################

# Online Shopping 2

age = 15
payment_method = False
items = 4

if age >= 18: # Adult
    if payment_method == True: 
        if items > 0:
            print("Sie dürfen zur Kasse!")
        else:
            print("Sie benötigen Produkte bevor Kasse!")
    else:
        print("Sie müssen Bezahlungsmethode eingeben!")
else: # kid
    print("Sie sind zu jung.")


#################################


# Ideal Solution is in 03_Ubung3_OnlineShop_idealsolution