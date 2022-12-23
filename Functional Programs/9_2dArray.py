"""
@Author: Bhupinder Singh
@Date: 2022-12-14
@Last Modified by: Bhupinder Singh
@Last Modified time: 2022-12-14
@Title : "Python program to print a 2d array by taking a user input.”
"""
import numpy as np

def main():
  try:
    arr_size = int(input("enter the size of array"))
    x=int(input("enter the x-dimension of an array"))
    y=int(input("enter the y-dimension of an array"))

  except ValueError:
        print("Only Integer values are allowed")

  arr= np.arange(arr_size).reshape(x,y)

  for i in range(x):
    for j in range(y):
      arr[i][j]=int(input("Enter arr elements : "))


  print(arr)

if __name__== "__main__":
  main()  
