import numpy as np
a = np.array([10,20,30,40,50])
avg = np.mean (a)
print (avg)
b = np.arange(101)

print (np.sum(b))
print (np.max(b))
print (np.min(b))
print (np.mean(b))

print ("2d array")
twod = np.array ([
    [1,2,3],
    [7,4,8]
    
])

print (np.ndim(twod))
print (np.size(twod))
print (np.shape(twod))

marks = np.array([45,78,92,35,88,65,95])


m =marks [marks>70]
print(m)

    
