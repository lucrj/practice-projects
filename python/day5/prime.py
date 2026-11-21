def cprime(n):
    """check if n is a prime number"""
    if n <= 1 :
        return False
    for i in range (2, int (n** 0.5) + 1):
        if n % i == 0:
            return False
    return True

n  = int (input("enter a number : "))
if cprime(n):
    print (f"{n} is a prime number ")
else  :
    print (f"{n} is not a prime number ")
    