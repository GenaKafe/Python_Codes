from pathlib import Path
import os

#.\ current ..\ a folder up     /// dir - shows all the directories
# import pathlib
# return pathlib.Path().home()
# Current working directory: pathlib.Path.cwd() 
# (similar to the value returned by os.getcwd function)


print(Path(__file__).parent) # Shows the absolute file path & makes the file path dynamic
# c:\Users\Administrator\Desktop\All_Files_Together\Python\Gena_Codes\13_Pathlib\Pathlib_Ex

os.chdir(Path(__file__).parent) # it changes the cursor to our current file ???
# c:\Users\Administrator\Desktop\All_Files_Together\Python\Gena_Codes\13_Pathlib\Pathlib_Ex
print(Path(__file__).parent)
#c:\Users\Administrator\Desktop\All_Files_Together\Python\Gena_Codes\13_Pathlib\Pathlib_Ex

# os.chdir(r".\Python\Gena_Codes")

# The below should return that No such file or dierctory 'textfile.txt'.
# r --> read and w --> write
with open(r"textfile.txt") as file: 
    print("Hallo")

APP_FOLDER = Path(__file__).parent
print(APP_FOLDER)

mylist = list(APP_FOLDER.glob("*.txt")) # built-in function for collecting all the ending with .txt
print(mylist)

for file in mylist:  # for each file you are going to print/ read/ open the files
    print(file)

file = Path(__file__).name # pathlib_test.py
print(file) # Shows the name of the file 

file = Path(__file__).name.split(".")[0] # [0] displays the name of the file
print(file) # pathlib_test

file = Path(__file__).name.split(".")[1] # [1] displays the extension of the file
print(file) # py



"""dir --> in the terminal shows me all the folders"""