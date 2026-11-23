p1 = str (input("enter the paragraph : "))

characters  = {char for char in p1.replace(" ","")  }
print (characters)
print ("number of characters :",len(characters))

print ("total words :" , (sum (1 for n in p1.split())))
vowels = ["a","e","i","o","u"]
print ("total vowels  : ", (sum ( 1 for n in p1.lower()if n in  vowels)))

freq = {}

for n in p1.replace(" ","") :
  freq [n] = freq.get(n,0)+1

print ("the frequency of each word :", freq)

v  = max(freq.values())
maxkeys = [k for  k,p in freq.items() if p==v ]

print ("word: " , maxkeys ,"frequency : ", v )


 
