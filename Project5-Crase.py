"""
Program: Project5
Author: Cole Crase
Calculating the object's momentum by inputting the object's mass and
multiplying it by its velocity.
"""
mass = float(input("Enter the object's mass (in kilogram): "))
velocity = float(input("Enter the object's velocity (in meters per second): "))
result = mass * velocity
print("The momentum of this object is", result)
