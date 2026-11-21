def largest(a,b):
    if a==b :
        return "both numbers are equal"
    elif a>b  :
        return a 
    else :
        return b
n = int (input ("enter a number : "))
m = int (input ("enter another number : "))

print ("Largest number is : ", largest(n,m))