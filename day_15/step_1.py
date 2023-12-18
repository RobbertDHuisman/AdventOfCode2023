import pandas as pd

run = "input"
df = pd.read_csv(f"day_15/{run}.csv", delimiter=" ", names=["all"])

df["split"] = df["all"].str.split(pat=",")
df["result"] = pd.Series([[] for i in range(len(df))])
total = 0

for i in range(0, len(df["split"][0])):
    number = 0
    for j in range(0, len(df["split"][0][i])):
        number += ord(df["split"][0][i][j:j+1])
        number *= 17
        number %= 256
    df["result"][0].append(number)    
    total += number

print(df)
print(total)
