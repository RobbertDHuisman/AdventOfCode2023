import pandas as pd
import math

df = pd.read_csv("day_11/input.csv", names=["alles"])

empty_rows = []
empty_columns = []
distance = 1000000
sum = 0
done = 0

df["empty"] = df.loc[df["alles"].str.contains("#")]
for i in range(0,len(df)):
    if pd.isna(df["empty"][i]):
        empty_rows.append(i)

for i in range(0, len(df["alles"][0])):
    df["row"]=df["alles"].str.slice(i, i+1)
    if "#" not in df["row"].unique():
        empty_columns.append(i)

df["aantal"] = df["alles"].str.count('#')
df_coordinates = pd.Series([[] for i in range(df["aantal"].sum())])

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

for i in range(0, len(df_coordinates)):
    for j in range(1, len(df_coordinates) - i):
        for k in range(0,2):
            extensions = 0
            if k == 0:
                for l in empty_rows:
                    if df_coordinates[i][k] < l < df_coordinates[i+j][k] or df_coordinates[i][k] > l > df_coordinates[i+j][k]:
                        extensions += 1
            if k == 1:
                for l in empty_columns:
                    if df_coordinates[i][k] < l < df_coordinates[i+j][k] or df_coordinates[i][k] > l > df_coordinates[i+j][k]:
                        extensions += 1     
            sum += abs(df_coordinates[i][k] - df_coordinates[i+j][k]) + extensions * (distance - 1)

print(sum)