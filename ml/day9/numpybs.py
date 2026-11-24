import numpy as np 
a =  np.arange(51)

d = a[a%2==0]
print(d)

###ex2###
marks =  np.array([12,45,65,90,76,80])

print (marks[(marks > 60 ) & (marks <=90  )])

### ex 3 ###

marks[marks < 40] = 0

print (marks)