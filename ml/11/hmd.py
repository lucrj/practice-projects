import pandas as pd 

data =  {
    "name" : ["alex","dario","lucy","maria","paul"],
    "age" : [21,31,None,5,90],
    "index" : [1,4,5,None,3],
    "marks" : [100,None,95,62,30]
}
df= pd.DataFrame(data)

print(df.isna().sum())

print (df.isna().any(axis=0 ))
##df.dropna(inplace=True)
print(df)

df["marks"]=df["marks"].fillna(df["marks"].mean())

print ("df after avg fill \n", df)

bata =  {
    "name" : ["alex","dario","lucy","maria","paul"],
    "age" : [21,31,None,5,90],
    "index" : [1,4,5,None,3],
    "marks" : [100,None,95,62,30]
}
ff= pd.DataFrame(bata)
ff.dropna(inplace=True)
print ("new dataframe after drop na :\n",ff)