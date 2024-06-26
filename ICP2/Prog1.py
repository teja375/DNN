# Write a program that takes two strings from the user: first_name, last_name. Pass these variables to
# fullname function that should return the (full name).
# o For example:
# ▪ First_name = “your first name”, last_name = “your last name”
# ▪ Full_name = “your full name”

First_name=input("Enter your first name:")
last_name=input("Enter the last name:")
Full_name= First_name + last_name # string concatenation 
print("your full name :" + Full_name)


# Write function named “string_alternative” that returns every other char in the full_name string.
# Str = “Good evening”
# Output: Go vnn
# Note: You need to create a function named “string_alternative” for this program and call it from
# main function.
str=Full_name
def string_alernative(str):
    Output=""
    for index,char in enumerate (str): # enumerating the string
        if index % 2 == 0: # here we are taking the alternate charcters
            Output += char #appending to the output 
    return Output

resultstr=string_alernative(str)
print(resultstr)