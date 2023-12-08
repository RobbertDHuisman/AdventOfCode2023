import pandas as pd

df  = pd.read_csv("day_7/input.csv", delimiter=" ")
dict = {"2":"0", "3":"1", "4":"2", "5":"3", "6":"4", "7":"5", "8":"6", "9":"7", "T":"8" ,"J":"9", "Q":"10", "K":"11", "A":"12"}
lengte = len(df)

for i in range(0,5):
    df[f"{i+1}"] = df["hand"].str.slice(i,i+1)
    df.replace({f"{i+1}":dict}, inplace=True)
    df[f"{i+1}"] = df[f"{i+1}"].astype(int)

df["count"] = pd.Series([[] for i in range(lengte)])
df["unique"] = ""
df["strength"] = 0
df["length"] = 0
df["multiply"] = 0

for i in range(0, lengte):
    df["unique"][i]= set(df["hand"][i])

    for j in df["unique"][i]:
        df["count"][i].append(df["hand"][i].count(j))
        df["length"][i] += 1

    if df["length"][i] == 1:
        df["strength"][i] = 6
    
    elif df["length"][i] == 2 and 4 in df["count"][i]:
        df["strength"][i] = 5

    elif df["length"][i] == 2 and 3 in df["count"][i]:
        df["strength"][i] = 4    

    elif df["length"][i] == 3 and 3 in df["count"][i]:
        df["strength"][i] = 3
    
    elif df["length"][i] == 3 and 2 in df["count"][i]:
        df["strength"][i] = 2

    elif df["length"][i] == 4:
        df["strength"][i] = 1

    elif df["length"][i] == 5:
        df["strength"][i] = 0


# df = df.sort_values(by=["strength", "1", "2", "3", "4", "5"], ascending=[False,False,False,False,False,False], ignore_index=True)
df = df.sort_values(by=["strength", "1", "2", "3", "4", "5"], ascending=False, ignore_index=True)

for i in range(0, lengte):
    df["multiply"][i] = lengte - i

df["product"] = df["bid"] * df["multiply"]
print(df)
print(sum(df["product"]))