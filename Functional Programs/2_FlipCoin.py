"""
@Author: Bhupinder Singh
@Date: 2022-12-12
@Last Modified by: Bhupinder Singh
@Last Modified time: 2022-12-12
@Title : Python program to calculate the percentage of heads and tails in a coin toss”
"""


import random


def cointoss():
    """

    Description :
        This function is used to compute the percentage of heads and tails in a coin toss.
    Parameters :
        none
    Return:
        none

    """
    numOfHeads = 0
    numOfTails = 0
    numOfFlips = int(input("Enter a number for number of flips: "))

    if (numOfFlips > 0):
        for i in range(numOfFlips):
            flipResult= random.randint(0, 1)
            if (flipResult > 0.5):
                numOfHeads+=1
                print("Head")
            else:
                print("Tail")
                numOfTails+=1

        percentHead = numOfHeads / numOfFlips * 100
        percentTail = numOfTails / numOfFlips * 100
        print("Percentage of heads:", percentHead)
        print("Percentage of tails:", percentTail)            
                    
                
    else:
        print("Please enter a positive number")
                        
            
cointoss()

