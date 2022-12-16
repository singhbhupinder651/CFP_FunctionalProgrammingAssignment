"""
@Author: Bhupinder Singh
@Date: 2022-12-12
@Last Modified by: Bhupinder Singh
@Last Modified time: 2022-12-12
@Title : "Python program to print the sum of the harmonic series”
"""


num=int(input("Enter a number to get harmonic series and its Nth harmonic value: "))
            
if (num > 0):

    count = 1
    while (count < num):
    
        print("1/" , count , " + ",end=" ")
        count+=1
    
    print("1/" , num)

    sum = 0
    for i in range(1,num):
    
        sum += 1 / i
    
    print("Value of Nth Harmonic is: " , sum)

else:

    print("Enter a number greater than zero")
