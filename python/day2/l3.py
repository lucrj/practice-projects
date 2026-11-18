l,m,n = map(int, input("Enter three numbers separated by spaces: ").split())

if l >=m and l >= n:
    print(f"{l} is the largest number.")
elif m >= l and m >= n:
    print (f"{m} is the largest number")
else :
    print (f"{n} is the largets number ")
    