"""
@Author: Bhupinder Singh
@Date: 2022-12-12
@Last Modified by: Bhupinder Singh
@Last Modified time: 2022-12-12
@Title : Python Program to print a table of the powers of 2^N.”
"""


power= lambda x,y: x**y

exponentN=int(input("Enter a number to print 2^N table: "))

if (exponentN >= 0 and exponentN < 31):

    for i in range(exponentN):
        print(power(2, i))
else:

    print("Please enter a number between 0 and 31, excluding 31")

