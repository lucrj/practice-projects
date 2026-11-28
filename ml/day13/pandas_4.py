import pandas as pd

df = pd.read_csv("student_data.csv")

print (df)

print(df.head())
print(df.tail())
print(df.shape)
print(df.size)
print(df.columns)
print(df.info())
print(df.describe())
print(df.dtypes)

df["marks"] = df["marks"]+5
df.to_csv("updated_students.csv",index = False)

print (df)



