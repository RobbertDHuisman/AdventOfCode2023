import pandas as pd
import re

df = pd.read_csv("day_3/input.csv")

df["numbers"] = df["input"].str.findall(r'[0-9]{1,4}')
df["stars"] = df["input"].str.findall(r'\*')
df["index"] = pd.Series([[] for i in range(140)])
df["index_star"] = pd.Series([[] for i in range(140)])
df["length"] = pd.Series([[] for i in range(140)])
df["substr1"] = pd.Series([[] for i in range(140)])
df["substr2"] = pd.Series([[] for i in range(140)])
df["substr3"] = pd.Series([[] for i in range(140)])
df["substr1_star"] = pd.Series([[] for i in range(140)])
df["substr2_star"] = pd.Series([[] for i in range(140)])
df["substr3_star"] = pd.Series([[] for i in range(140)])
df["counts"] = pd.Series([[] for i in range(140)])
df["counts_index"] = pd.Series([[] for i in range(140)])
df["counts_star"] = pd.Series([[] for i in range(140)])
df["in_product"] = pd.Series([[] for i in range(140)])
df["sum"] = 0

regexp = re.compile(r'[\*]')
regexp_num = re.compile(r'\d')
regexp_middle = re.compile(r'\d\*\d')
regexp_top_bottom = re.compile(r'\d.\d')

for i in range(0, 140):
    for j in range(0, len(df["numbers"][i])):
            length = len(df["numbers"][i][j])
            df["length"][i].append(len(df["numbers"][i][j]))

            if j == 0:
                index = df["input"][i].find(df["numbers"][i][j])
            else:
                index = df["input"][i].find(df["numbers"][i][j], df["index"][i][j-1] + df["length"][i][j-1])

            df["index"][i].append(index)
            if index == 0:
                start_index = 0
            else:
                start_index = index - 1

            if i == 0:
                df["substr2"][i].append(df["input"][i][int(start_index) : int(index + length + 1)])
                df["substr3"][i].append(df["input"][i+1][int(start_index) : int(index + length + 1)])       
                if regexp.search(df["substr2"][i][j]) or regexp.search(df["substr3"][i][j]):
                    df["counts"][i].append(df["numbers"][i][j])
                    df["counts_index"][i].append(df["index"][i][j])

            if 0 < i < 139: 
                df["substr1"][i].append(df["input"][i-1][int(start_index) : int(index + length + 1)])
                df["substr2"][i].append(df["input"][i][int(start_index) : int(index + length + 1)])
                df["substr3"][i].append(df["input"][i+1][int(start_index) : int(index + length + 1)])
                if regexp.search(df["substr1"][i][j]) or regexp.search(df["substr2"][i][j]) or regexp.search(df["substr3"][i][j]):
                    df["counts"][i].append(df["numbers"][i][j])
                    df["counts_index"][i].append(df["index"][i][j])

            if i == 139: 
                df["substr1"][i].append(df["input"][i-1][int(start_index) : int(index + length + 1)])
                df["substr2"][i].append(df["input"][i][int(start_index) : int(index + length + 1)])        
                if regexp.search(df["substr1"][i][j]) or regexp.search(df["substr2"][i][j]):
                    df["counts"][i].append(df["numbers"][i][j])
                    df["counts_index"][i].append(df["index"][i][j])

for i in range(0, 140):
    for k in range(0, len(df["stars"][i])):

        if k == 0:
            index_star = df["input"][i].find(df["stars"][i][k])            
        else:
            index_star = df["input"][i].find(df["stars"][i][k], df["index_star"][i][k-1] + 1)

        df["index_star"][i].append(index_star)

        if index_star == 0:
            start_index_star = 0
        else:
            start_index_star = index_star - 1

        if 0 < i < 139:
            df["substr1_star"][i].append(df["input"][i-1][int(start_index_star) : int(index_star + 2)])
            df["substr2_star"][i].append(df["input"][i][int(start_index_star) : int(index_star + 2)])
            df["substr3_star"][i].append(df["input"][i+1][int(start_index_star) : int(index_star + 2)])      

            if (regexp_num.search(df["substr1_star"][i][k]) and regexp_num.search(df["substr2_star"][i][k])):
                df["counts_star"][i].append(df["index_star"][i][k])
                for l in range(-1,1):
                    for j in range(0, len(df["counts_index"][i+l])):
                        if df["index_star"][i][k] -1 <= df["counts_index"][i+l][j] <= df["index_star"][i][k] + 1 \
                        or df["index_star"][i][k] -1 <= df["counts_index"][i+l][j] + len(str(df["counts"][i+l][j]))  - 1 <= df["index_star"][i][k] + 1:
                            df["in_product"][i].append(df["counts"][i+l][j])

            if (regexp_num.search(df["substr2_star"][i][k]) and regexp_num.search(df["substr3_star"][i][k])):
                df["counts_star"][i].append(df["index_star"][i][k])
                for l in range(0,2):
                    for j in range(0, len(df["counts_index"][i+l])):
                        if df["index_star"][i][k] -1 <= df["counts_index"][i+l][j] <= df["index_star"][i][k] + 1 \
                        or df["index_star"][i][k] -1 <= df["counts_index"][i+l][j] + len(str(df["counts"][i+l][j])) -1 <= df["index_star"][i][k] + 1:
                            df["in_product"][i].append(df["counts"][i+l][j])  

            if (regexp_num.search(df["substr1_star"][i][k]) and regexp_num.search(df["substr3_star"][i][k])):
                df["counts_star"][i].append(df["index_star"][i][k])
                for l in range(-1,3,2):
                    for j in range(0, len(df["counts_index"][i+l])):

                        # print(f"for i={i}, j]{j}, l={l}")  
                        # print(df["index_star"][i][k])
                        # print(df["counts_index"][i+l][j])
                        # print(df["length"][i+l][j])                        
                        if df["index_star"][i][k] -1 <= df["counts_index"][i+l][j] <= df["index_star"][i][k] + 1 \
                        or df["index_star"][i][k] -1 <= df["counts_index"][i+l][j] + len(str(df["counts"][i+l][j])) -1 <= df["index_star"][i][k] + 1:
                            df["in_product"][i].append(df["counts"][i+l][j])  

            if regexp_top_bottom.search(df["substr1_star"][i][k]):
                for j in range(0, len(df["counts_index"][i-1])):
                    if df["counts_index"][i-1][j] == df["index_star"][i][k] + 1 \
                    or df["index_star"][i][k] -1 == df["counts_index"][i-1][j] + len(str(df["counts"][i-1][j])) -1:
                        df["counts_star"][i].append(df["index_star"][i][k])
                        df["in_product"][i].append(df["counts"][i-1][j])  

            if regexp_middle.search(df["substr2_star"][i][k]):
                for j in range(0, len(df["counts_index"][i])):
                    if df["counts_index"][i][j] == df["index_star"][i][k] + 1 \
                    or df["index_star"][i][k] -1 == df["counts_index"][i][j] + len(str(df["counts"][i][j])) -1:
                        df["counts_star"][i].append(df["index_star"][i][k])
                        df["in_product"][i].append(df["counts"][i][j])  

            if regexp_top_bottom.search(df["substr3_star"][i][k]):
                for j in range(0, len(df["counts_index"][i+1])):
                    if df["counts_index"][i+1][j] == df["index_star"][i][k] + 1 \
                    or df["index_star"][i][k] -1 == df["counts_index"][i+1][j] + len(str(df["counts"][i+1][j])) -1:
                        df["counts_star"][i].append(df["index_star"][i][k])
                        df["in_product"][i].append(df["counts"][i+1][j])                                                  

for i in range(0,140):
    for j in range(0, len(df["in_product"][i]), 2):
        df["sum"][i] = df["sum"][i] + int(df["in_product"][i][j]) * int(df["in_product"][i][j+1])

df["total"] = df["sum"].sum()

with pd.option_context(
    # 'display.max_columns', None 
    # ,
                        'display.max_rows', None
    ,
                        'max_colwidth', None
                       ):
    # print(df.loc[16])
    # print(df[["counts_star", "in_product"]])
    print(df)
#     # print(df.loc[125])

# # print(df["counts"])

