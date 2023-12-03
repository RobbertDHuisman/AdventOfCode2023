import pandas as pd

red  = 12
green = 13
blue = 14

df = pd.read_csv("day_2/input.csv", delimiter= ': ', engine='python')
df["game"] = df["game"].replace(r'(Game )', "", regex=True).astype(int)

df["red"] = df["values"].str.findall(r'([0-9]{1,3}) red', )
df["green"] = df["values"].str.findall(r'([0-9]{1,3}) green', )
df["blue"] = df["values"].str.findall(r'([0-9]{1,3}) blue', )

print(df)


df = df[["red", "green", "blue"]]
df["max_red"] = 0
df["max_green"] = 0
df["max_blue"] = 0

for i in range(0, 100):
    df["red"][i] = [int(s) for s in df["red"][i]]
    df["green"][i] = [int(s) for s in df["green"][i]]
    df["blue"][i] = [int(s) for s in df["blue"][i]]
    df["max_red"][i] = max(df["red"][i])
    df["max_green"][i] = max(df["green"][i])
    df["max_blue"][i] = max(df["blue"][i])

df["product"] = df["max_red"].astype(int) * df["max_green"].astype(int) * df["max_blue"].astype(int)
df["som"] = df["product"].sum()

with pd.option_context('display.max_rows', None):
    print(df)
