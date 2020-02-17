# Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.

firstn = input("First name: ")
lastn = input("Last name: ")

print(firstn[::-1] + " " + lastn[::-1])