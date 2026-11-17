p = int (input("Enter a the principal amount: "))
r = float (input("Enter the rate of interest(per annum): "))   
t = int (input("Enter the time in years: "))

si = (p * r * t) / 100  

print ("The simple interest is: ", si)
print ("The total amount to be paid is: ", p + si)
