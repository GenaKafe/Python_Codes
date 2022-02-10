for x in ["Thomas", "Ingo", "Frank", "Sara"]:

    if x == "Frank":
        break # exits the loop completly
    else:
        print(x)

print("End of For loop")


###############################################


for x in ["Thomas", "Ingo", "Frank", "Sara"]:

    if x == "Frank":
        break # exits the loop completely

    print(x)

print("End of for loop 2")

print()


###############################################
for x in range(100): # [0->99]
    if x == 5: 
        break
    print(x)

################################################

temperature = 8
status = True
while status == True:
    print("temperature:", temperature)

    if temperature == 27:
        print("Hallo 27")
        break

    if temperature == 20:
        print("Hallo 20")
        break

    if temperature == 15:
        print("Hallo 15")
        break

    if temperature == 7:
        status = False

    temperature -= 1

print("End of Code 1")