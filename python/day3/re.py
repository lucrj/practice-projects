n = int (input ("enter a number : "))
d = 0

while n > 0:
     new = n % 10
     d = d*10 + new 
     n = n // 10
    
print (d)
