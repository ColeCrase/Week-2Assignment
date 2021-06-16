"""
Program: Project3
Author: Cole Crase
Calculating the total charge for a customer's video rentals.
"""
new = int(input("Enter the number of new movies being rented: "))
old = int (input("Enter the number of old movies being rented: "))
result = (new * 3.00) + (old * 2.00)
print("The total cost is", "$", result)
