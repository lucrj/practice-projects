import pandas as pd

df = pd.read_csv("student_data.csv")

print(df.head(2))
print(df.shape)
print (df["student_name"],df["marks"])
print(df["marks"].mean())
print(df.iloc[df["marks"].idxmax()])
print(df.iloc[df["marks"]<80])

df.to_csv("result.csv", index = False)

