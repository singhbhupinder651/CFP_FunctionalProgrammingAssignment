"""

@Author: Bhupinder Singh
@Date: 2022-12-12
@Last Modified by: Bhupinder Singh
@Last Modified time: 2022-12-12
@Title : Python Program to take User Input and print the username on console”

"""


user_name_length= 0
while(user_name_length<3):
    user_name= input("Enter your name: ")
    user_name_length=len(user_name)

    if(user_name_length<3):
        print("Length of name must be more than or equal to 3")
        
print("Hello " + user_name + ",How are you?")