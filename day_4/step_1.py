import pandas as pd

df = pd.read_csv("day_4/input.csv", delimiter= ': ', engine='python')
df = df["numbers"].str.split(pat="|", expand=True)
df["win"] = df[df.columns[0]].str.findall(r'[0-9]{1,2}')
df["card"] = df[df.columns[1]].str.findall(r'[0-9]{1,2}')
df["points"] = 0

print(len(df["card"][0]))

for h in range(0,196):
    for i in range(0, len(df["card"][h])):
        for j in range(0, len(df["win"][h])):
            if df["card"][h][i] == df["win"][h][j]:
                if df["points"][h] == 0:
                    df["points"][h] = 1
                else:
                    df["points"][h] = df["points"][h] * 2       

df["sum"] = df["points"].sum()

print(df)