import pandas as pd

df = pd.read_csv("day_4/input.csv", delimiter= ': ', engine='python')
df = df["numbers"].str.split(pat="|", expand=True)
df["win"] = df[df.columns[0]].str.findall(r'[0-9]{1,2}')
df["card"] = df[df.columns[1]].str.findall(r'[0-9]{1,2}')
df["numberofcards"] = 1
df["points"] = 0

for h in range(0,196):
    for i in range(0, len(df["card"][h])):
        for j in range(0, len(df["win"][h])):
            if df["card"][h][i] == df["win"][h][j]:
                df["points"][h] = df["points"][h]+1

    for k in range(0, df["points"][h]):
        df["numberofcards"][h + k + 1] = df["numberofcards"][h + k + 1] + df["numberofcards"][h]



df["sum"] = df["numberofcards"].sum()

with pd.option_context(
    # 'display.max_columns', None 
                        'display.max_rows', None
                       ):
    print(df[["numberofcards", "points"]])

print(df["sum"])