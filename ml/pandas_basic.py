import pandas as pd 

data =  {
    "name" : ["alex","dario","lucy","maria","paul"],
    "age" : [21,31,32,5,90],
    "index" : [1,4,5,2,3],
    "marks" : [100,46,95,62,30]
}

df = pd.DataFrame(data)
print (df)

### acessing columns ###
print ("acessing columns")
print (df["name"])
print (df["age"])

print (df[["name","age"]])

###basic operations ###
print("basic ops")
print (df["marks"].mean())
print (df["marks"].sum())
print (df["marks"].max())
print (df["marks"].min())

##filtering ##
print ("filering")
print (df[df["marks"] > 45])
print (df[df["age"] >= 45])

print ("student with highest marks : ")
print ( df.loc[df["marks"].idxmax()])