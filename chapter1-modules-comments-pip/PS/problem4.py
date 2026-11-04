
import os

# Specify the directory path
path = "C:/Users/dell/Desktop/Code"

# Get all files and folders
contents = os.listdir(path)

# Print directory contents
for item in contents:
    print(item)
