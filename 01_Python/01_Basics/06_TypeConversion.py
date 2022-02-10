# int()
# float()
# str()
# bool()
user_input = ""

user_input = input("Enter a number:  ")
print(user_input, type(user_input)) # 50 <class 'str'>

# Conversion to integer
user_input = int(user_input)
print(user_input, type(user_input)) # 50 <class 'int'>

# Conversion to float
user_input = float(user_input)
print(user_input, type(user_input)) # 50.0 <class 'float'>

# Conversation to string
x = 6
y = 6
print("The result is:" + str(x + y))