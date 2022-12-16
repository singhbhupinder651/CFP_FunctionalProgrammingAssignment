"""
@Author: Bhupinder Singh
@Date: 2022-12-15
@Last Modified by: Bhupinder Singh
@Last Modified time: 2022-12-16
@Title : Python program to find to find the roots of the quadratic equation.

"""

def roots(a,b,c):

    """
    Description : 
        To find to find the roots of the quadratic equation
    Parameters :
        a: constant used in quadratic equation
        b: constant used in quadratic equation
        c: constant used in quadratic equation
    Return:
        none
    """

    
    delta=b*b-4*a*a*c
    Root1=(-b+(delta**0.5))/(2*a)
    Root2= (-b-(delta**0.5))/(2*a)
    print(f"Roots of the given quadratic equation are : {Root1},{Root2}")

def main():
    try:
        a=int(input("Enter the value of first constant for the quadratic equation : "))
        b=int(input("Enter the value of second constant for the quadratic equation : "))
        c=int(input("Enter the value of third constant for the quadratic equation : "))

    except ValueError:
        print("Only Integer values are allowed")    
    roots(a,b,c)    

if __name__== "__main__":
    main()