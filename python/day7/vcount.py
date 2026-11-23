n1 =  str (input("enter a word : "))


vcount = 0


for n in  n1 :
    if n.lower() in  "aeiou" :
        vcount += 1

print (vcount)
