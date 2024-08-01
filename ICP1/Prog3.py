x=int(input("Enter your marks between 0 and 100:"))

def marks(x):
    if x>=90 and x<=100:
        return "A"
    elif x>=80 and x<90:
        return "B"
    elif x>=70 and x<80:
        return "C"
    elif x>=60 and x<70:
        return "D"
    else:
        return "F"


print("Grade:",marks(x))