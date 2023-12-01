import pandas as pd

df = pd.read_csv("day_1/input.csv")
# left
df["one"] = df["values"].str.find(r'one')
df["two"] = df["values"].str.find(r'two')
df["three"] = df["values"].str.find(r'three')
df["four"] = df["values"].str.find(r'four')
df["five"] = df["values"].str.find(r'five')
df["six"] = df["values"].str.find(r'six')
df["seven"] = df["values"].str.find(r'seven')
df["eight"] = df["values"].str.find(r'eight')
df["nine"] = df["values"].str.find(r'nine')
df["1"] = df["values"].str.find(r'1')
df["2"] = df["values"].str.find(r'2')
df["3"] = df["values"].str.find(r'3')
df["4"] = df["values"].str.find(r'4')
df["5"] = df["values"].str.find(r'5')
df["6"] = df["values"].str.find(r'6')
df["7"] = df["values"].str.find(r'7')
df["8"] = df["values"].str.find(r'8')
df["9"] = df["values"].str.find(r'9')

df = df.replace(-1, 999)
df["min"] = df.min(axis=1, numeric_only=True)
df["first"] = ""

for i in range(0, 1000):
    if df["min"][i] == df["one"][i]:
        df["first"][i] = 1

    if df["min"][i] == df["1"][i]:
        df["first"][i] = 1

    if df["min"][i] == df["two"][i]:
        df["first"][i] = 2

    if df["min"][i] == df["2"][i]:
        df["first"][i] = 2

    if df["min"][i] == df["three"][i]:
        df["first"][i] = 3

    if df["min"][i] == df["3"][i]:
        df["first"][i] = 3

    if df["min"][i] == df["four"][i]:
        df["first"][i] = 4

    if df["min"][i] == df["4"][i]:
        df["first"][i] = 4

    if df["min"][i] == df["five"][i]:
        df["first"][i] = 5

    if df["min"][i] == df["5"][i]:
        df["first"][i] = 5

    if df["min"][i] == df["six"][i]:
        df["first"][i] = 6

    if df["min"][i] == df["6"][i]:
        df["first"][i] = 6

    if df["min"][i] == df["seven"][i]:
        df["first"][i] = 7

    if df["min"][i] == df["7"][i]:
        df["first"][i] = 7

    if df["min"][i] == df["eight"][i]:
        df["first"][i] = 8

    if df["min"][i] == df["8"][i]:
        df["first"][i] = 8

    if df["min"][i] == df["nine"][i]:
        df["first"][i] = 9

    if df["min"][i] == df["9"][i]:
        df["first"][i] = 9

# right
df["one"] = df["values"].str.rfind(r'one')
df["two"] = df["values"].str.rfind(r'two')
df["three"] = df["values"].str.rfind(r'three')
df["four"] = df["values"].str.rfind(r'four')
df["five"] = df["values"].str.rfind(r'five')
df["six"] = df["values"].str.rfind(r'six')
df["seven"] = df["values"].str.rfind(r'seven')
df["eight"] = df["values"].str.rfind(r'eight')
df["nine"] = df["values"].str.rfind(r'nine')
df["1"] = df["values"].str.rfind(r'1')
df["2"] = df["values"].str.rfind(r'2')
df["3"] = df["values"].str.rfind(r'3')
df["4"] = df["values"].str.rfind(r'4')
df["5"] = df["values"].str.rfind(r'5')
df["6"] = df["values"].str.rfind(r'6')
df["7"] = df["values"].str.rfind(r'7')
df["8"] = df["values"].str.rfind(r'8')
df["9"] = df["values"].str.rfind(r'9')

df["max"] = df.max(axis=1, numeric_only=True)
df["last"] = ""


################# last
for i in range(0, 1000):
    if df["max"][i] == df["one"][i]:
        df["last"][i] = 1

    if df["max"][i] == df["1"][i]:
        df["last"][i] = 1

    if df["max"][i] == df["two"][i]:
        df["last"][i] = 2

    if df["max"][i] == df["2"][i]:
        df["last"][i] = 2

    if df["max"][i] == df["three"][i]:
        df["last"][i] = 3

    if df["max"][i] == df["3"][i]:
        df["last"][i] = 3

    if df["max"][i] == df["four"][i]:
        df["last"][i] = 4

    if df["max"][i] == df["4"][i]:
        df["last"][i] = 4

    if df["max"][i] == df["five"][i]:
        df["last"][i] = 5

    if df["max"][i] == df["5"][i]:
        df["last"][i] = 5

    if df["max"][i] == df["six"][i]:
        df["last"][i] = 6

    if df["max"][i] == df["6"][i]:
        df["last"][i] = 6

    if df["max"][i] == df["seven"][i]:
        df["last"][i] = 7

    if df["max"][i] == df["7"][i]:
        df["last"][i] = 7

    if df["max"][i] == df["eight"][i]:
        df["last"][i] = 8

    if df["max"][i] == df["8"][i]:
        df["last"][i] = 8

    if df["max"][i] == df["nine"][i]:
        df["last"][i] = 9

    if df["max"][i] == df["9"][i]:
        df["last"][i] = 9


df["sum"] = df["first"].astype(str) + df["last"].astype(str)
df["total"] = sum(df["sum"].astype(int))
df = df[["values", "first", "last","sum", "total"]]
with pd.option_context('display.max_rows', None):
    print(df)