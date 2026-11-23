n1 = str (input ("enter a string : "))
n,m = 0,len(n1)
p = True
while (n < m):
    if n1 [n] != n1 [m] :
        p = False 
        break 
    n+=1
    m-=1
print ("the entered string is a palindrome :" , p)
