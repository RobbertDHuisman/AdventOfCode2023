import pandas as pd
import re

df = pd.read_csv("day_3/input.csv")

df["numbers"] = df["input"].str.findall(r'[0-9]{1,4}')
df["index"] = pd.Series([[] for i in range(140)])
df["length"] = pd.Series([[] for i in range(140)])
df["substr1"] = pd.Series([[] for i in range(140)])
df["substr2"] = pd.Series([[] for i in range(140)])
df["substr3"] = pd.Series([[] for i in range(140)])
df["counts"] = pd.Series([[] for i in range(140)])
df["sum"] = 0

regexp = re.compile(r'[^.\d]')

for i in range(0, 140):
    for j in range(0, len(df["numbers"][i])):
        length = len(df["numbers"][i][j])
        df["length"][i].append(len(df["numbers"][i][j]))

        if j == 0:
            index = df["input"][i].find(df["numbers"][i][j])
        else:
            index = df["input"][i].find(df["numbers"][i][j], df["index"][i][j-1] + df["length"][i][j-1])

        df["index"][i].append(df["input"][i].find(df["numbers"][i][j]))
        if index == 0:
            start_index = 0
        else:
            start_index = index - 1

        if i == 0:
            df["substr2"][i].append(df["input"][i][int(start_index) : int(index + length + 1)])
            df["substr3"][i].append(df["input"][i+1][int(start_index) : int(index + length + 1)])
            if regexp.search(df["substr2"][i][j]) or regexp.search(df["substr3"][i][j]):
                df["counts"][i].append(df["numbers"][i][j])
                df["sum"][i] = df["sum"][i] + int(df["numbers"][i][j])

        if 0 < i < 139: 
            df["substr1"][i].append(df["input"][i-1][int(start_index) : int(index + length + 1)])
            df["substr2"][i].append(df["input"][i][int(start_index) : int(index + length + 1)])
            df["substr3"][i].append(df["input"][i+1][int(start_index) : int(index + length + 1)])
            if regexp.search(df["substr1"][i][j]) or regexp.search(df["substr2"][i][j]) or regexp.search(df["substr3"][i][j]):
                df["counts"][i].append(df["numbers"][i][j])
                df["sum"][i] = df["sum"][i] + int(df["numbers"][i][j])

        if i == 139: 
            df["substr1"][i].append(df["input"][i-1][int(start_index) : int(index + length + 1)])
            df["substr2"][i].append(df["input"][i][int(start_index) : int(index + length + 1)])
            if regexp.search(df["substr1"][i][j]) or regexp.search(df["substr2"][i][j]):
                df["counts"][i].append(df["numbers"][i][j])
                df["sum"][i] = df["sum"][i] + int(df["numbers"][i][j])                

df["total"] = df["sum"].sum()

with pd.option_context(
    # 'display.max_columns', None 
    # ,
    #                     'display.max_rows', None
    # ,
                        'max_colwidth', None
                       ):
    print(df)
    # print(df["counts"])
    # print(df.loc[125])

# print(df["counts"])

