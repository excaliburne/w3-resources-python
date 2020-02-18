# Write a Python program to print the calendar of a given month and year.
# Note : Use 'calendar' module.

import calendar

m = int(input("Give me a month in digit like '04', '05': "))
y = int(input("Give me a year: "))

print(calendar.month(y, m))