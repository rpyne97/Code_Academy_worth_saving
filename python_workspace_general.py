## Working directory
# Import the os library
import os
# Get cwd
os.getcwd()
# List files in cwd
for file_name in os.listdir('.'):
    print(file_name)

# Rename a file
os.rename('welcome.txt', 'not_welcome.txt')

# Remove a file
os.remove('not_welcome.txt')









