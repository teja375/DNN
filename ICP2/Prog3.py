# 3. Write a program, which reads heights (inches.) customers into a list and convert these heights to
# centimeters in a separate list using:
# 1) Nested Interactive loop.
# 2) List comprehensions
# Example: L1: [150,155, 145, 148]
# Output: [68.03, 70.3, 65.77, 67.13]

height_in=[]
customers=int(input("Enter the no of customers:"))
for i in range(customers):
    height_ins= float(input("Enter the customers height ".format(i+1)))
    height_in.append(height_ins)

height_cm=[i*2.54 for i in height_in]
print("height in inches",height_in)
print("height in centimeters",height_cm)