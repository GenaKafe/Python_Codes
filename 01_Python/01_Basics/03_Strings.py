
# Definition a string
course = "Python"
course = 'Python'
print(course)

# Multi-line String
message = """
Hallo Thomas, 
wie geht es dir?
Lange nicht gesehen. 
Schöne Grüße, 
Mattias
"""
print(message)

# String Function
len(course) # length of the variable course

print(len(course)) # 6


# Slicing
course = "Python Programmierung"
print(course[0]) # P
print(course[4]) # o
print(course[20]) # g
print(course[-1]) # g
print(course[-4]) # r
print(course[0:5]) # Pytho
print(course[7:20]) # Programmierun
print(course[0:6]) # Python
print(course[7:500]) # Programmierung
print(course[7:]) # From 7: to the end.  --> Programmierung
print(course[:6]) # From Begin: to 5. --> Python
print(course[:]) # Python Programmierung
print(course) # Python Programmierung
print(course[-14:-1]) # Programmierun
print(course[-14:0]) # empty line
print(course[-14:]) # Programmierung
print(course[-1:-14]) # empty line
print(), print()

# Escaping via \, \n: New Line, \t: TAB
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Mohamed sagte 'Guten Morgen' heute!
# Mohamed sagte "Guten Morgen" heute!
# Mohamed sagte \Guten Morgen\ heute!

print('Mohamed sagte \'Guten Morgen\' heute !') # Mohamed sagte 'Guten Morgen' heute !
print("Mohamed sagte \"Guten Morgen\" heute !") # Mohamed sagte "Guten Morgen" heute !
print("Mohamed sagte \\Guten Morgen\\ heute !") # Mohamed sagte \Guten Morgen\ heute !

print()

# Alternative
print("Mohamed sagte 'Guten Morgen' heute !")
print('Mohamed sagte "Guten Morgen" heute !')

print()

# Two Prints
print("Python")
print("Java")

print()

# Alternative with one print
print("Python\nJava") # \n: new line
print("Python\tJava") # \t: TAB


# String Formatting
first_name = "Mohamed"
last_name = "Ibrahim"

# String concatenation
# full_name = fist_name + "\t" + last_name # MohamedIbrahim
# full_name = first_name + " " + last_name # MohamedIbrahim
full_name = first_name + last_name # MohamedIbrahim

print(full_name)

print(first_name , last_name) # additional comma in between: Mohamed Ibrahim
print(first_name + last_name) # MohamedIbrahim

print("first_name last_name") # first_name last_name

print(f"First Name: {first_name} - Last Name: {last_name} !")
# First Name: Mohamed -  Last Name: Ibrahim !

# String Building
full_name = f"Welcome, First Name: {first_name} , Last Name: {last_name}"
print(full_name) # Welcome, First Name: Mohamed , Last Name: Ibrahim


# String Methods (DOT Function)
course = "   pyThON proGraMmieRunG   "

print(course.upper()) #    PYTHON PROGRAMMIERUNG   
print(course.lower()) #    python programmierung
print(course.title()) #    Python progrmammierung
print(course.capitalize()) #    Python programmierung
print(course.strip()) # removes the spaces at the beginning and the end of the string: pyThON proGraMmieRunG
print(course.find("pro")) # 10, index of p
print(course.replace("py","jy")) #    jyThON proGraMmieRunG   


# Method Chain
print(course.upper().lower().strip())
print(course.strip().upper().lower())

user_name = input("Enter your name: ").title()
print(user_name)

course = "   pyThON proGraMmieRunG   "
course.upper().strip()
course.strip().upper()



print(course.strip().upper()) 

course = course.strip().upper() # PYTHON PROGRAMMIERUNG
print(course)
