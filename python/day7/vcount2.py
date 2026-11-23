n1 = str (input ("enter the word :  "))

vowels = ['a','e','i','o','u']

print (sum(1 for  char in n1 if char.lower() in vowels ))
