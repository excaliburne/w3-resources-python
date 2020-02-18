# Write a Python program to get the difference between a given number and 17, 
# if the number is greater than 17 return double the absolute difference.

n = int(input("Input a number: "))

if n > 17:
    result = (n - 17) * 2
else: 
    result = n - 17

print(result)