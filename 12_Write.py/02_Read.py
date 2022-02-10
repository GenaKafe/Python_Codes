
file = open("myfile.txt", mode="r")
content = file.read() # reads the whole content in one variable
print(content)

file.close()


# Alternative
with open("myfile2.txt", mode="r", encoding="UTF-8") as file: 
    content = file.read()
    print(content)