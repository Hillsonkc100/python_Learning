# write a python program to print the content of a directory using the os module

import os

path = input("Enter directory path: ")

try:
    for item in os.listdir(path):
        print(item)
except Exception as e:
    print(f"Error: {e}")
