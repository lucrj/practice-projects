numbers = [1,2,3,4,5,6,7,8,9,1,3,5,7,9]

freq = {}

for i in range (len(numbers)):
    freq[numbers[i]] = freq.get(numbers[i], 0) + 1

    

print (freq)