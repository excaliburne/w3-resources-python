# Write a Python program to get the volume of a sphere with radius 6.

r = int(input("Enter a radius: "))

def getVolume(radius):
    volume = (4/3) * 3.14 * (radius * radius * radius)
    print(volume)

getVolume(r)