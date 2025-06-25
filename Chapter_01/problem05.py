# label the program written in problem 4 with comments

import os  # Import the os module to interact with the operating system

# Ask the user to enter a directory path
path = input("Enter directory path: ")

try:
    # Loop through and print each item in the specified directory
    for item in os.listdir(path):
        print(item)
except Exception as e:
    # Print an error message if something goes wrong (e.g., path doesn't exist or permission denied)
    print(f"Error: {e}")
