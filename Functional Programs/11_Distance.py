"""
@Author: Bhupinder Singh
@Date: 2022-12-15
@Last Modified by: Bhupinder Singh
@Last Modified time: 2022-12-15
@Title : Python program to find distance of the given point from origin
"""


import math

try:
    x=int(input("Enter the value for x-axis"))
    y=int(input("Enter the value for y-axis"))

except ValueError:
        print("Only Integer values are allowed")
distance = math.pow((x*x +y*y),0.5)

print(f"Distance of the given point from origin is = {distance}")