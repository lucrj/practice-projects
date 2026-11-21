marks = [75,80,65,90,85,70]

print ("avg: " ,sum(marks)/len(marks))

print ("max : ",max(marks))

print ("min : ",min(marks))

for i in range(len(marks)):
    if marks[i] > 75 :
        print("marks above 75 :" + str(marks[i]))

newmarks = [m for m in marks if m > 75]

print (newmarks)