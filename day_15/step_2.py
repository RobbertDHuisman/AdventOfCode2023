import pandas as pd
import re

run = "input"
df_input = pd.read_csv(f"day_15/{run}.csv", delimiter=" ", names=["all"])
df=pd.DataFrame()

df["split"] = df_input["all"].str.split(pat=",")
df["box"] = pd.Series([[[] for i in range(256)] for i in range(len(df))])
df["box_number"] = pd.Series([[] for i in range(len(df))])
df["box_input"] = pd.Series([[] for i in range(len(df))])
df["label"] = pd.Series([[] for i in range(len(df))])
df["power"] = pd.Series([[] for i in range(len(df))])
df["result"] = pd.Series([[] for i in range(len(df))])
total = 0

for i in range(0, len(df["split"][0])):
    number = 0
    if df["split"][0][i][-1] == '-':
        remove = 0
        label = df["split"][0][i][0:len(df["split"][0][i])-1]
        for j in range(0, len(label)):
            number += ord(label[j:j+1])
            number *= 17
            number %= 256
        for k in range(0, len(df["box"][0][number])):
            if label == df["box"][0][number][k][0:len(df["box"][0][number][k]) - 2]:
                 remove = 1
                 to_remove = df["box"][0][number][k]

        if remove == 1:
            df["box"][0][number].remove(to_remove)    

    else: 
        label = df["split"][0][i][0:len(df["split"][0][i])-2]
        power = df["split"][0][i][len(df["split"][0][i])-1: len(df["split"][0][i])]
        box_input = label + " " + power
        for j in range(0, len(label)):
            number += ord(label[j:j+1])
            number *= 17
            number %= 256

        vervangen = 0
        for k in range(0, len(df["box"][0][number])):
            if label == df["box"][0][number][k][0:len(df["box"][0][number][k]) - 2]:
                df["box"][0][number][k] = box_input
                vervangen = 1

        if vervangen == 0:
            df["box"][0][number].append(box_input)

for i in range(0, len(df["box"][0])):
    result = 0
    for j in range(0, len(df["box"][0][i])):
        result += (i+1) * (j+1) * int(df["box"][0][i][j][-1])
    df["result"][0].append(result)
    total += result

print(df)
print(total)