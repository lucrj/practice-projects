import pandas as pd 

data =  {
    "name" : ["alex","dario","lucy","maria","paul"],
    "age" : [21,31,32,5,90],
    "index" : [1,4,5,2,3],
    "marks" : [100,46,95,62,30]
}
df= pd.DataFrame(data)
print("sorted students : \n", df.sort_values(by ="marks"))

print ("top 3 students wrt marks : \n",df.sort_values(by="marks").head(3))

df ["rank"] = df["marks"].rank(ascending = False , method = "min")

print ()
print ("students btw marks of 50 and 90 :")
print ()


print (df.loc[df.loc[(df["marks"]>50) & (df["marks"]<90),"marks"].idxmax()])

print ("sorted wrt age  : \n" , df.sort_values(by = "age"))