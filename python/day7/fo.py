file = open("student.txt","w")
file.write ("lucky , 23 , cse ")
file.close()

file = open("student.txt","a")
file.write (",jss stu")
file.close()

with open ("student.txt" , "r")  as file :
    content = file.read()
    print (content)
