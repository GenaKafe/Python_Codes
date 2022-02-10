import os
from pathlib import Path

# Get the path of the file --> Its parent
APP_FOLDER = Path(__file__).parent

# Change the directory of terminal to the parent folder (analog to cd....)
os.chdir(APP_FOLDER)

with open("file1.txt", mode="a+") as f: 
    f.write("Hello Mustafa\n")

"""
When the app is with external data (outside python), we definetelly need this template. 
"""