"""
@Author: Bhupinder Singh
@Date: 2022-12-14
@Last Modified by: Bhupinder Singh
@Last Modified time: 2022-12-14
@Title : "Python program to print Distinct Coupon Numbers”
"""


import numpy as np
import random


def CouponNumber(N):

    """
    Description:
        A function to get the random numbers from random library and store only the distinct numbers to an array.
    Parameters:
        n: Array Size
    Return:
        none
    """


    array = np.arange(N)
    for i in range(N):
        random_generate= random.randint(999,10000)
                
        if (i == 0):       
            array[i] = random_generate        
        else:        
            j = 0
            check = 0
            while (j < i):
            
                if (array[j] == random_generate):
                    check = 1
                j+=1
            
            if (check == 0):
                array[i] = random_generate
            else:
                i-=1
        
    
    print("Distinct Coupons Are:")
    for i in range(N):
        print(array[i])

def main():
    try:
        Number=int(input("How many distinct coupon numbers do you want to generate "))
        CouponNumber(Number) 
    except ValueError:
        print("Only Integer values are allowed")       

if __name__ == "__main__":
    main()