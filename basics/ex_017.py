# Write a Python program to test whether a number is within 100 of 1000 or 2000

n = int(input("Input a number: "))

if n < 100:
    print("You number is below 100")
elif n >= 100 and n < 1000:
    print("Your number is bewteen 100 and 2000")
elif n >= 1000 and n < 2000:
    print("Your number is between 1000 and 2000")
else: 
    print("Your number is above 2000")

