"""
@Author: Bhupinder Singh
@Date: 2022-12-15
@Last Modified by: Bhupinder Singh
@Last Modified time: 2022-12-15
@Title : Python program that prints the wind chill.
"""

import math


def WindChill(t,v):

    
    """
    Description :
        Function that prints the value of wind chill      
    Parameters :
        t: Temperature
        v: wind Speed
    Return:
        none
    """

    
    w=35.74+0.6215*t+(0.4275*t - 35.75)*(math.pow(v,0.16))
    print(f" Wind chill is : {w}")

def main():

    try:
        t=int(input("Enter the value of temp: "))
        if(t>50):
            print("value of temp should be less than 50")
        v=int(input("Enter the value of wind speed : "))
        if(v>120 or v<3):
            print("the wind speed should be between 3 and 120")

    except ValueError:
        print("Only Integer values are allowed")        
    WindChill(t,v)    

if __name__== "__main__":
    main()

