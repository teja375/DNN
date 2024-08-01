str=input("Enter the input string:")
if len(str)>=2:
    str=str[:-2]
else:
    str=str[:-1]
print(str[::-1])




