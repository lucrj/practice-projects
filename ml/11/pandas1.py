import pandas as pd 

data =  {
    "name" : ["alex","dario","lucy","maria","paul"],
    "age" : [21,31,32,5,90],
    "index" : [1,4,5,2,3],
    "marks" : [100,46,95,62,30]
}

df = pd.DataFrame(data)

print("sorted : ")
print (df.sort_values (by="marks"))
print ("sorted descending : ")
print (df.sort_values (by="marks" , ascending=False))

print ("rank ")

df["rank"] =  df["marks"].rank(ascending = False,method = "min")

print (df["rank"])

print ("sorted using rank : ")

print (df.sort_values(by= "rank"))

print ("sorted using rank in descending order : ")

print (df.sort_values(by ="rank",ascending = False))