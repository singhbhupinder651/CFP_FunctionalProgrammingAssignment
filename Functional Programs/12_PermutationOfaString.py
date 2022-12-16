"""
@Author: Bhupinder Singh
@Date: 2022-12-15
@Last Modified by: Bhupinder Singh
@Last Modified time: 2022-12-15
@Title : Python program to return all permutation of a String using iterative method and Recursion method
"""


list1=[]
partial = []

def swap(ch, i, j):

    """
    Description:
        Function to swap two characters in a character array
    Parameters:
        ch: character list
        i: first index
        j:second index
    Return:
        none
    """

    temp = ch[i]
    ch[i] = ch[j]
    ch[j] = temp
 
 

def RecursivePermutations(ch, curr_index=0):

    """
    Description:
        Recursive function to generate all permutations of a string 
    Parameters:
        ch: character list
        curr index : to keep the track of index in a list.
    Return:
        none
    """

    
    if curr_index == len(ch) - 1:
        list1.append(''.join(ch))
        
 
    for i in range(curr_index, len(ch)):
        swap(ch, curr_index, i)
        RecursivePermutations(ch, curr_index + 1)
        swap(ch, curr_index, i)

    

def IterativePermutations(s):


    """
    Description:
        Iterative function to generate all permutations of a string in Python
    Parameters:
        s: Input List
    Return:
        none
    """
 
    # base case
    if not s:
        return []
 
    # create a list to store (partial) permutations
    
 
    # initialize the list with the first character of the string
    partial.append(s[0])
 
    # do for every character of the specified string
    for i in range(1, len(s)):
 
        # consider previously constructed partial permutation one by one
 
        # iterate backward
        for j in reversed(range(len(partial))):
 
            # remove the current partial permutation from the list
            curr = partial.pop(j)
 
            # Insert the next character of the specified string into all
            # possible positions of current partial permutation.
            # Then insert each of these newly constructed strings into the list
 
            for k in range(len(curr) + 1):
                partial.append(curr[:k] + s[i] + curr[k:])
 
    print(partial, end='') 

def main():
        
    
    s = 'ABC'
    flag=0
    RecursivePermutations(list(s))
    print(list1, end='')
    print()
    IterativePermutations(s)
    for item in list1:
        if(item in partial):
            flag=0
        else:
            flag=1    

    if(flag==0):
        print()
        print("List returned by both the methods are same")

    if(flag==1):
        print("List returned by both the methods are not same")    

if __name__ == '__main__':
    main()
 
 
