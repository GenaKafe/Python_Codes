
# 1. Open
f = open("myfile.txt", mode= "a+", encoding="UTF-8") # a+: append and create the file if not available
# f or something else. It is a name of variable.

# 2. Write content
f.write("Python\n")
f.write("Java\n")

for x in range(10):

    f.write(f"{x}\n")

# 3. Close file
f.close()


# Alternative
with open("myfile2.txt", mode= "a+", encoding="UTF-8") as f: 
    f.write("Hello Python\n")
