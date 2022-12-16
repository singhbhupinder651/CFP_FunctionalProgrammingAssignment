"""
@Author: Bhupinder Singh
@Date: 2022-12-14
@Last Modified by: Bhupinder Singh
@Last Modified time: 2022-12-14
@Title : "Python program to Simulates a gambler”
"""


import random


def gamble(stake,goal,numberOfBets):


    """
    Description:
        A function to print the Win count ,percentage of win and percentage of lose in a gamble
    Parameters:
        Stake: money used to put on stake
        Goal : goal set by the user to achieve in betting
        Number of times: Number of times user want to bet
    Return:
        none
    """


    win=1
    win_count=0
    lose_count=0
    bet_count=numberOfBets

    while(stake<goal and stake!=0 and bet_count!=0):

        bet_result=random.randint(0,1)
        if(bet_result==win):
            win_count+=1
            stake+=1
        else:
            lose_count+=1
            stake-=1
        bet_count-=1
    
    win_percentage= win_count/numberOfBets*100
    lose_percentage=lose_count/numberOfBets*100
    print("Win Count = " , win_count)
    print("percentage of win = ", win_percentage)
    print("percentage of lose = ", lose_percentage)   


def main():
    
    try:
        stake=int(input("Enter the amount you want to keep on stake = "))
        goal=int(input("Enter the amount you want to keep as a goal = "))
        numberOfBets= int(input("Enter how many times you want to place a bet = "))   
        gamble(stake,goal,numberOfBets)

    except ValueError:
        print("Only Integer values are allowed")


if __name__ == "__main__":
    main()

