import pandas as pd

df = pd.read_csv("day_1/input.csv")
print(df)

df["numbers"] = df["values"].replace(r'([A-z])', "", regex=True)
df["first"] = df["numbers"].str[0]
df["last"] = df["numbers"].str[-1]
df["sum"] = df["first"] + df["last"]
df["total"] = sum(df["sum"].astype(int))
# df["sum"] = df["numbers"].str[0].astype(int), df["numbers"].str[-1].astype(int))
print(df)