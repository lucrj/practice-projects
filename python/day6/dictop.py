students = {
    "alex": 85,
    "sophia": 90,
    "arvin": 78,
    "emma": 43,
    "maria": 78
}

print ("avg of the marks of the students is ", sum(students.values())/len(students))

print ("max marks is ", max(students.values()))

print ("students  with marks aboove 80 are ", [k for k,v in students.items() if v >80])

print ("the number of students that passed" , sum(1 for i, k in students.items() if k > 40))
