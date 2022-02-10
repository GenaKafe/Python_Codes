# Online Shopping - My version

# 1. Phase: User Input

age = int(input("Wie alt sind Sie?  "))

if age < 18:
    print("Sie sind zu jung.")
else: 
    print("Wilkkommen bei Ihren Online Shop")
    payment_method = False

    if payment_method == True:
        print("Sie können zur Kasse gehen.")
    else:
        print("Sie müssen Bezahlungsmethode eingeben.")
