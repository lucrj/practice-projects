def factorial (n):
    if n == 0:
        return 1
    else :
         return factorial (n-1)*n

n = int (input ("enter a number : "))

print ("factorial of ",n, " is ", factorial (n))