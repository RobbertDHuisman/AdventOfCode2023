import pandas as pd
import re

df = pd.read_csv("day_12/input.csv", delimiter=" ", names=["gears", "numbers"])
df["sets"] = df["numbers"].str.split(pat=',')
df["options"] = 0
df["position"] = pd.Series([[] for i in range(len(df))])
df["points"] = pd.Series([[] for i in range(len(df))])
df["position"] = pd.Series([[] for i in range(len(df))])

for i in range(0, len(df)):
    length_set = 0
    for j in df["sets"][i]:
        length_set += int(j)

    if length_set + len(df["sets"][i]) - 1 == len(df["gears"][i]):
        df["options"][i] = 1

df["questionmarks"] = df["gears"].str.findall(r'\?')
pointhash = [".", "#"]

for i in range(0, len(df)):
    if df["options"][i] != 1:

        start = 0
        points = []
        gears_found = []
        for j in df["questionmarks"][i]:
            df["position"][i].append(df["gears"][i].find(j, start))
            start = df["gears"][i].find(j, start) + 1
            new_points = []
            
            if points == []:
                new_points = pointhash
            else:
                for k in points:
                    for l in pointhash:
                        new_points.append(k+l)
            points = new_points

        for m in points:
            gears_option = df["gears"][i]
            replace_position = 0
            gears_length = []
            for n in df["position"][i]:
                gears_option = gears_option[0:n] + m[replace_position:replace_position+1] + gears_option[n+1:len(df["gears"][i])]
                replace_position += 1
            gears_found = re.findall(pattern=r'[#]{1,100}', string=gears_option)
            for o in gears_found:
                gears_length.append(str(len(o)))
            if gears_length == df["sets"][i]:
                df["options"][i] = df["options"][i] + 1
    
        print(f"------------------------------------------- i={i} en m={m} ----------------------------------------------------")

sum = df["options"].sum()
print(df)
print(sum)