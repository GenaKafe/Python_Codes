print(10 > 3) # True
print(10 >= 3) # True

print(10 < 3) # False
print(10 <= 3) # False


# '=' : Zuweisung / Assignment
# '==' : Vergleich / Comparison

x = 10
y = 5

print(x == y) # False, Vergleich ob x gleich y ist / if x equals y
print(x != y) # True, Vergleich ob x nicht gleich y ist / if x not equals to y

#########################################################
# and , or, 

x = 10
y = 5
print( (x == 10) (y == 5) ) # True
print( (x == 9) and (y == 5) ) # False

print( (x == 9) or (y == 5)) # True
print( (x == 9) or (y == 5)) # False


print( (x != 9) or (y != 2) )  # True

# not (Nigierung) T-> False   F-> True
anwesend = True
print(anwesend) # True
print(not anwesend) # False