# exit infinite loop --> ctrl + C = cancel

temperature = 35

while temperature > 30: 
    print("Klima an: ", temperature)
    temperature -= 1

print("Ende")
print()
#######################################

# FIXME: there is no input and therefore nothing happens
command = ""

while command != "exit":
    command = input("> ")
    print("Echo:", command)
print("Ende 2")

print()

#######################################
# print all numbers from 1 to 10

number = 1

while number < 11:
    print(number)
    number += 1
print("Ende 3")
