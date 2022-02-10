import random

# float
print(random.random()) # float number 0-1 - randomly generated
print(random.uniform(2,10)) # float between 2-10

# integer
print(random.randint(2,20)) # integer between 2-20 --> includes the end point

print(random.randrange(2,20)) # integer between 2-20
print(random.randrange(2,20,2)) # integer between 2-20, step = 2

# Selection
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
teilnehmerliste = ["Thomas", "Ingo", "Sara", "Lena", "Jana", "Matthias"]

# Single Choice 
print(random.choice(teilnehmerliste))

# Multiple choice --> with duplication k: count of required elements (always use k!)
print(random.choices(teilnehmerliste, k = 3)) # ['Lena', 'Thomas', 'Matthias']
print(random.choices(teilnehmerliste, k = 30)) # ['Lena', 'Thomas', 'Matthias' ......, 'Lena', 'Thomas', 'Matthias']

# Multiple choices --> without duplication k: count of required elements (always use k!)
print(random.sample(teilnehmerliste, k = 4)) # ['Thomas', 'Lena', 'Jana', 'Sara']

# Examples
print(random.choices(range(100), k = 10)) # [57, 92, 2, 63, 61, 72, 22, 95, 21, 40]

# Shuffling
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
numbers = [1,2,3,4,5,6,7,8,9]
print(numbers) # [1, 2, 3, 4, 5, 6, 7, 8, 9]

random.shuffle(numbers) # changes the orginal order !! 
print("Shffled: ", numbers) # Shffled:  [4, 1, 3, 6, 9, 2, 7, 8, 5] 


""" Python has a built-in module that you can use to make random numbers.
The random module has a set of methods.
We need that when we want to teach the software to other possibilities. 
Machine learning - to try something out. 


Shuffle a list (reorganize the order of the list items). 
"""
