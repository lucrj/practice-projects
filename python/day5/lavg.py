

n = int (input("enter size of list : "))

number = [0] * n
def average (number) :
    return (sum(number)/len(number))

for i in range (n) :
    number[i] = int(input("enter the element :"))

print ("the list is :", number)
print ("the list avg is : ", average(number))