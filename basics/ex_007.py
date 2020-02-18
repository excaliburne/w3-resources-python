# Write a Python program to accept a filename from the user and print the extension of that. 
# Sample filename : abc.java
# Output : java

import os

filen = input("Enter a file name: ")
filename, file_extension = os.path.splitext(filen)

print(file_extension)

