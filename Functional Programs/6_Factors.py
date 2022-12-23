"""
@Author: Bhupinder Singh
@Date: 2022-12-12
@Last Modified by: Bhupinder Singh
@Last Modified time: 2022-12-12
@Title : "Python program to print prime factors”
"""


import math


def primeFactors(n):


    """
    Description:
        A function to print all prime factors of a given number n
    Parameters:
        n:The number n for which this function will print the prime factors
    Return:
        none
    """

     
    # Print the number of two's that divide n
    while n % 2 == 0:
        print(2)
        n = n / 2
         
    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3,int(n**0.5)+1,2):
         
        # while i divides n , print i and divide n
        while n % i== 0:
            print(i)
            n = n / i
             
    # Condition if n is a prime
    # number greater than 2
    if n > 2:
        print(n)
         
 
number=int(input("Enter the number to which you want to get the prime factors"))
primeFactors(number)

          