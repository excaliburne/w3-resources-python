# Write a Python program which accepts the radius of a circle from the user and compute the area.

def basic(r):
    area = 3*3.14 *r*r
    return area

r = int(input("enter the value of radius: "))
print(basic(r))