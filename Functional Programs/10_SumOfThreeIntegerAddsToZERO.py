"""
@Author: Bhupinder Singh
@Date: 2022-12-14
@Last Modified by: Bhupinder Singh
@Last Modified time: 2022-12-14
@Title : "Python program to find three elements whose sum is equal to zero”
"""
 
 
import numpy as np


def findTriplets(arr, n):


    """
    Description:
        A function that Prints all triplets in arr[] with 0 sum
    Parameters:
        n: Array Size 
        arr: input array
    Return:
        none
    """

    triplet_count=0
    found = False
    for i in range(0, n-2):
 
        for j in range(i+1, n-1):
 
            for k in range(j+1, n):
 
                if (arr[i] + arr[j] + arr[k] == 0):
                    print(arr[i], arr[j], arr[k])
                    triplet_count+=1
                    found = True
 
    # If no triplet with 0 sum
    # found in array
    if (found == False):
        print(" not exist ")
 
 

if __name__ == "__main__":

    try:  
        arr_size = int(input("Enter the size of array"))

    except ValueError:
        print("Only Integer values are allowed") 
        
    arr= np.arange(arr_size)

    for i in range(arr_size):
        arr[i]=int(input("Enter array element"))


    findTriplets(arr,arr_size)