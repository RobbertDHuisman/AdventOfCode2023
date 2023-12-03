import pandas as pd

red  = 12
green = 13
blue = 14

df = pd.read_csv("day_2/input.csv", delimiter= ': ', engine='python')
df["game"] = df["game"].replace(r'(Game )', "", regex=True).astype(int)

df["red"] = df["values"].str.findall(r'([2-9][0-9])|(1[3-9]) red', )
df["green"] = df["values"].str.findall(r'([2-9][0-9])|(1[4-9]) green', )
df["blue"] = df["values"].str.findall(r'([2-9][0-9])|(1[5-9]) blue', )

df["som"] = 0
print(df)

for i in range(0, 100):
    if i == 0:
        if df["red"][i] == [] and df["green"][i] == [] and df["blue"][i] == []:
            df["som"][i] = df["game"][i]

        else:
            df["som"][i] = df["som"][i-1]

    else:
        if df["red"][i] == [] and df["green"][i] == [] and df["blue"][i] == []:
            df["som"][i] = df["game"][i] + df["som"][i-1]

        else:
            df["som"][i] = df["som"][i-1]

print(df) 

