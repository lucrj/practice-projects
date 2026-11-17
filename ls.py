name = str (input ("Enter your login id   :  "))
password = str (input ("Enter your password :  "))

age = input ("Enter your age :  ")
age = int (age)
if (age>=18):
    if (name =="admin"and password == "admin"):
       print ("you are permitted")
    else :  print ("access denied , invalid pssword or login id ")
    
else : print (" youu are underaged , not permitted")


