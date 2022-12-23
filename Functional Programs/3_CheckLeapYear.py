"""
@Author: Bhupinder Singh
@Date: 2022-12-12
@Last Modified by: Bhupinder Singh
@Last Modified time: 2022-12-12
@Title : Python program to check whether a year is leap year or not”
"""


def CheckLeapYear():

          
    """
    Description:
        This function is used to compute whether a year is leap year or not.
    Parameters:
        none
    Return:
        none
    """


    year=int(input("Enter a four digit number to determine if its a leap year:"))

    if (year > 999 and year < 10000):
    
        if((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
        
            print(year," is a leap year")
        
        else:
        
            print(year," is not a leap year")
    else:
    
        print("Please enter a four digit number")


CheckLeapYear()            
