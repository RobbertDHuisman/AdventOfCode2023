import pandas as pd
import math

df = pd.read_csv("day_11/input.csv", names=["alles"])

df["empty"] = df.loc[df["alles"].str.contains("#")]
for i in range(0,len(df)):
    if pd.isna(df["empty"][i]):
        df.loc[i+0.5] = df["alles"][i]

df = df.sort_index().reset_index(drop=True)
columns_done = 0

for i in range(0, len(df["alles"][0])):
    df["row"]=df["alles"].str.slice(i+columns_done, i+columns_done+1)
    if "#" not in df["row"].unique():
        df["alles"] = df["alles"].str.slice(0,i+columns_done) + "." + df["alles"].str.slice(i+columns_done, len(df["alles"][0]))
        columns_done += 1

df["aantal"] = df["alles"].str.count('#')
df_coordinates = pd.Series([[] for i in range(df["aantal"].sum())])
done = 0

for i in range(0, len(df)):
    previous = 0
    for j in range(0, df["aantal"][i]):
        if j == 0:
            df_coordinates[done].append(i)
            df_coordinates[done].append(df["alles"][i].find("#"))
            previous = df["alles"][i].find("#", previous) + 1
            done += 1
        else:
            df_coordinates[done].append(i)
            df_coordinates[done].append(df["alles"][i].find("#", previous))
            previous = df["alles"][i].find("#", previous) + 1
            done += 1

sum = 0

for i in range(0, len(df_coordinates)):
    for j in range(1, len(df_coordinates) - i):
        for k in range(0,2):
            sum += abs(df_coordinates[i][k] - df_coordinates[i+j][k])

print(sum)