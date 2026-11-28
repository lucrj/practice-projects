import pandas as pd
data =  {
    "name" : ["alex","dario","lucy","maria","paul"],
    "dept" : ["cs","it","cs","cs","it"],
    "age" : [21,31,None,5,90],
    "index" : [1,4,5,None,3],
    "marks" : [100,50,95,62,30]
}
df = pd.DataFrame(data)
print (df.groupby("dept")["marks"].agg(["mean","max","count","sum"]))
print ("dept with highest avg marks :\n" , df.groupby("dept")["marks"].mean().idxmax())

