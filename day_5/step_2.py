import pandas as pd

df  = pd.read_csv("day_5/seeds2.csv", delimiter=" ")
df1 = pd.read_csv("day_5/seed_to_soil.csv", delimiter=" ")
df2 = pd.read_csv("day_5/soil_to_fertilizer.csv", delimiter=" ")
df3 = pd.read_csv("day_5/fertilizer_to_water.csv", delimiter=" ")
df4 = pd.read_csv("day_5/water_to_light.csv", delimiter=" ")
df5 = pd.read_csv("day_5/light_to_temperature.csv", delimiter=" ")
df6 = pd.read_csv("day_5/temperature_to_humidity.csv", delimiter=" ")
df7 = pd.read_csv("day_5/humidity_to_location.csv", delimiter=" ")

# df["seed_max"] = pd.Series([[] for i in range(10)])
df["new_range"] = 0
df["seed"] = pd.Series([[] for i in range(10)])
df["soil"] = pd.Series([[] for i in range(10)])
df["soil_done"] = pd.Series([[] for i in range(10)])
df["fertilizer"] = pd.Series([[] for i in range(10)])
df["fertilizer_done"] = pd.Series([[] for i in range(10)])
df["water"] = pd.Series([[] for i in range(10)])
df["water_done"] = pd.Series([[] for i in range(10)])
df["light"] = pd.Series([[] for i in range(10)])
df["light_done"] = pd.Series([[] for i in range(10)])
df["temperature"] = pd.Series([[] for i in range(10)])
df["temperature_done"] = pd.Series([[] for i in range(10)])
df["humidity"] = pd.Series([[] for i in range(10)])
df["humidity_done"] = pd.Series([[] for i in range(10)])
df["location"] = pd.Series([[] for i in range(10)])
df["min"] = 0

# seed
for i in range(0, len(df)):
    df["seed"][i] = [df["seed_min"][i].astype(int), df["seed_min"][i].astype(int) + df["range"][i].astype(int)]

# soil
for i in range(0, len(df)):
    for j in range(0, len(df["seed"][i]), 2):
        for h in range(0, len(df1)):
            # both min and max in same range
            if int(df1["seed"][h]) <= int(df["seed"][i][j]) <= int(df1["seed"][h]) + int(df1["range"][h]) \
                and int(df1["seed"][h]) <= int(df["seed"][i][j+1]) <= int(df1["seed"][h]) + int(df1["range"][h]):
                min = int(df["seed"][i][j]) + int(df1["soil"][h]) - int(df1["seed"][h])
                max = int(df["seed"][i][j+1]) + int(df1["soil"][h]) - int(df1["seed"][h])
                df["soil"][i].append(min)
                df["soil"][i].append(max)
                df["new_range"][i] = df["new_range"][i] + max - min

            # min in range, but max out of range
            if int(df1["seed"][h]) <= int(df["seed"][i][j]) <= int(df1["seed"][h]) + int(df1["range"][h]) \
                and int(df1["seed"][h]) + int(df1["range"][h]) < int(df["seed"][i][j+1]):
                min = int(df["seed"][i][j]) + int(df1["soil"][h]) - int(df1["seed"][h])
                max = int(df1["soil"][h]) + int(df1["range"][h])
                df["soil"][i].append(min)
                df["soil"][i].append(max)  
                df["new_range"][i] = df["new_range"][i] + max - min

            # # max in range, but min out of range
            if int(df["seed"][i][j]) < int(df1["seed"][h]) \
                and int(df1["seed"][h]) <= int(df["seed"][i][j+1]) <= int(df1["seed"][h]) + int(df1["range"][h]):
                min = int(df1["soil"][h])
                max = int(df["seed"][i][j+1]) + int(df1["soil"][h]) - int(df1["seed"][h])
                df["soil"][i].append(min)
                df["soil"][i].append(max)
                df["new_range"][i] = df["new_range"][i] + max - min

            # # min lower and max higher
            if int(df["seed"][i][j]) < int(df1["seed"][h]) \
                and int(df1["seed"][h]) + int(df1["range"][h]) < int(df["seed"][i][j+1]):
                min = int(df1["soil"][h])
                max = int(df1["soil"][h]) + int(df1["range"][h])
                df["soil"][i].append(min)
                df["soil"][i].append(max)
                df["new_range"][i] = df["new_range"][i] + max - min                         

df["new_range"] = 0

# # fertilizer
for i in range(0, len(df)):
    for j in range(0, len(df["soil"][i]), 2):
        for h in range(0, len(df2)):
            # both min and max in same range
            if int(df2["soil"][h]) <= int(df["soil"][i][j]) <= int(df2["soil"][h]) + int(df2["range"][h]) \
                and int(df2["soil"][h]) <= int(df["soil"][i][j+1]) <= int(df2["soil"][h]) + int(df2["range"][h]):
                min = int(df["soil"][i][j]) + int(df2["fertilizer"][h]) - int(df2["soil"][h])
                max = int(df["soil"][i][j+1]) + int(df2["fertilizer"][h]) - int(df2["soil"][h])
                df["fertilizer"][i].append(min)
                df["fertilizer"][i].append(max)
                df["soil_done"][i].append(df["soil"][i][j])
                df["soil_done"][i].append(df["soil"][i][j+1])
                df["new_range"][i] = df["new_range"][i] + max - min

            # min in range, but max out of range
            if int(df2["soil"][h]) <= int(df["soil"][i][j]) <= int(df2["soil"][h]) + int(df2["range"][h]) \
                and int(df2["soil"][h]) + int(df2["range"][h]) < int(df["soil"][i][j+1]):
                min = int(df["soil"][i][j]) + int(df2["fertilizer"][h]) - int(df2["soil"][h])
                max = int(df2["fertilizer"][h]) + int(df2["range"][h])
                df["fertilizer"][i].append(min)
                df["fertilizer"][i].append(max)  
                df["soil_done"][i].append(df["soil"][i][j])
                df["soil_done"][i].append(int(df2["soil"][h]) + int(df2["range"][h]))
                df["new_range"][i] = df["new_range"][i] + max - min

            # # max in range, but min out of range
            if int(df["soil"][i][j]) < int(df2["soil"][h]) \
                and int(df2["soil"][h]) <= int(df["soil"][i][j+1]) <= int(df2["soil"][h]) + int(df2["range"][h]):
                min = int(df2["fertilizer"][h])
                max = int(df["soil"][i][j+1]) + int(df2["fertilizer"][h]) - int(df2["soil"][h])
                df["fertilizer"][i].append(min)
                df["fertilizer"][i].append(max)
                df["soil_done"][i].append(df2["soil"][h])
                df["soil_done"][i].append(df["soil"][i][j+1])
                df["new_range"][i] = df["new_range"][i] + max - min

            # # min lower and max higher
            if int(df["soil"][i][j]) < int(df2["soil"][h]) \
                and int(df2["soil"][h]) + int(df2["range"][h]) < int(df["soil"][i][j+1]):
                min = int(df2["fertilizer"][h])
                max = int(df2["fertilizer"][h]) + int(df2["range"][h])
                df["fertilizer"][i].append(min)
                df["fertilizer"][i].append(max)
                df["soil_done"][i].append(df2["soil"][h])
                df["soil_done"][i].append(int(df2["soil"][h]) + int(df2["range"][h]))
                df["new_range"][i] = df["new_range"][i] + max - min   

for i in range(0, len(df)):
    for j in range(0, len(df["soil"][i]), 2):
        min = df["soil"][i][j]
        max = df["soil"][i][j+1]
        for k in range(0, len(df["soil_done"][i]), 2):
            for l in range(0, len(df["soil_done"][i]), 2):
                if min == df["soil_done"][i][l] and min != df["soil"][i][j+1]:
                    min = df["soil_done"][i][l+1]
                if max == df["soil_done"][i][l+1] and max != df["soil"][i][j]:
                    max = df["soil_done"][i][l]    

        if min != df["soil"][i][j+1]:
            df["fertilizer"][i].append(min)
        if max != df["soil"][i][j]:
            df["fertilizer"][i].append(max)
            df["new_range"][i] = df["new_range"][i] + max - min   

# with pd.option_context(
#                         'display.max_column', None
#     ,
#                         'max_colwidth', None
#                        ):
#     # print(df)
#     print(df[['range', 'new_range', "soil", 'soil_done']])

df["new_range"] = 0

# water
for i in range(0, len(df)):
    for j in range(0, len(df["fertilizer"][i]), 2):
        for h in range(0, len(df3)):
            # both min and max in same range
            if int(df3["fertilizer"][h]) <= int(df["fertilizer"][i][j]) <= int(df3["fertilizer"][h]) + int(df3["range"][h]) \
                and int(df3["fertilizer"][h]) <= int(df["fertilizer"][i][j+1]) <= int(df3["fertilizer"][h]) + int(df3["range"][h]):
                min = int(df["fertilizer"][i][j]) + int(df3["water"][h]) - int(df3["fertilizer"][h])
                max = int(df["fertilizer"][i][j+1]) + int(df3["water"][h]) - int(df3["fertilizer"][h])
                df["water"][i].append(min)
                df["water"][i].append(max)
                df["fertilizer_done"][i].append(df["fertilizer"][i][j])
                df["fertilizer_done"][i].append(df["fertilizer"][i][j+1])
                df["new_range"][i] = df["new_range"][i] + max - min

            # min in range, but max out of range
            if int(df3["fertilizer"][h]) <= int(df["fertilizer"][i][j]) <= int(df3["fertilizer"][h]) + int(df3["range"][h]) \
                and int(df3["fertilizer"][h]) + int(df3["range"][h]) < int(df["fertilizer"][i][j+1]):
                min = int(df["fertilizer"][i][j]) + int(df3["water"][h]) - int(df3["fertilizer"][h])
                max = int(df3["water"][h]) + int(df3["range"][h])
                df["water"][i].append(min)
                df["water"][i].append(max)  
                df["fertilizer_done"][i].append(df["fertilizer"][i][j])
                df["fertilizer_done"][i].append(int(df3["fertilizer"][h]) + int(df3["range"][h]))
                df["new_range"][i] = df["new_range"][i] + max - min

            # # max in range, but min out of range
            if int(df["fertilizer"][i][j]) < int(df3["fertilizer"][h]) \
                and int(df3["fertilizer"][h]) <= int(df["fertilizer"][i][j+1]) <= int(df3["fertilizer"][h]) + int(df3["range"][h]):
                min = int(df3["water"][h])
                max = int(df["fertilizer"][i][j+1]) + int(df3["water"][h]) - int(df3["fertilizer"][h])
                df["water"][i].append(min)
                df["water"][i].append(max)
                df["fertilizer_done"][i].append(df3["fertilizer"][h])
                df["fertilizer_done"][i].append(df["fertilizer"][i][j+1])
                df["new_range"][i] = df["new_range"][i] + max - min

            # # min lower and max higher
            if int(df["fertilizer"][i][j]) < int(df3["fertilizer"][h]) \
                and int(df3["fertilizer"][h]) + int(df3["range"][h]) < int(df["fertilizer"][i][j+1]):
                min = int(df3["water"][h])
                max = int(df3["water"][h]) + int(df3["range"][h])
                df["water"][i].append(min)
                df["water"][i].append(max)
                df["fertilizer_done"][i].append(df3["fertilizer"][h])
                df["fertilizer_done"][i].append(int(df3["fertilizer"][h]) + int(df3["range"][h]))
                df["new_range"][i] = df["new_range"][i] + max - min   

for i in range(0, len(df)):
    for j in range(0, len(df["fertilizer"][i]), 2):
        min = df["fertilizer"][i][j]
        max = df["fertilizer"][i][j+1]
        for k in range(0, len(df["fertilizer_done"][i]), 2):
            for l in range(0, len(df["fertilizer_done"][i]), 2):
                if min == df["fertilizer_done"][i][l] and min != df["fertilizer"][i][j+1]:
                    min = df["fertilizer_done"][i][l+1]
                if max == df["fertilizer_done"][i][l+1] and max != df["fertilizer"][i][j]:
                    max = df["fertilizer_done"][i][l]    

        if min != df["fertilizer"][i][j+1]:
            df["water"][i].append(min)
        if max != df["fertilizer"][i][j]:
            df["water"][i].append(max)
            df["new_range"][i] = df["new_range"][i] + max - min   

df["new_range"] = 0                    

# light
for i in range(0, len(df)):
    for j in range(0, len(df["water"][i]), 2):
        for h in range(0, len(df4)):
            # both min and max in same range
            if int(df4["water"][h]) <= int(df["water"][i][j]) <= int(df4["water"][h]) + int(df4["range"][h]) \
                and int(df4["water"][h]) <= int(df["water"][i][j+1]) <= int(df4["water"][h]) + int(df4["range"][h]):
                min = int(df["water"][i][j]) + int(df4["light"][h]) - int(df4["water"][h])
                max = int(df["water"][i][j+1]) + int(df4["light"][h]) - int(df4["water"][h])
                df["light"][i].append(min)
                df["light"][i].append(max)
                df["water_done"][i].append(df["water"][i][j])
                df["water_done"][i].append(df["water"][i][j+1])
                df["new_range"][i] = df["new_range"][i] + max - min

            # min in range, but max out of range
            if int(df4["water"][h]) <= int(df["water"][i][j]) <= int(df4["water"][h]) + int(df4["range"][h]) \
                and int(df4["water"][h]) + int(df4["range"][h]) < int(df["water"][i][j+1]):
                min = int(df["water"][i][j]) + int(df4["light"][h]) - int(df4["water"][h])
                max = int(df4["light"][h]) + int(df4["range"][h])
                df["light"][i].append(min)
                df["light"][i].append(max)  
                df["water_done"][i].append(df["water"][i][j])
                df["water_done"][i].append(int(df4["water"][h]) + int(df4["range"][h]))
                df["new_range"][i] = df["new_range"][i] + max - min

            # # max in range, but min out of range
            if int(df["water"][i][j]) < int(df4["water"][h]) \
                and int(df4["water"][h]) <= int(df["water"][i][j+1]) <= int(df4["water"][h]) + int(df4["range"][h]):
                min = int(df4["light"][h])
                max = int(df["water"][i][j+1]) + int(df4["light"][h]) - int(df4["water"][h])
                df["light"][i].append(min)
                df["light"][i].append(max)
                df["water_done"][i].append(df4["water"][h])
                df["water_done"][i].append(df["water"][i][j+1])
                df["new_range"][i] = df["new_range"][i] + max - min

            # # min lower and max higher
            if int(df["water"][i][j]) < int(df4["water"][h]) \
                and int(df4["water"][h]) + int(df4["range"][h]) < int(df["water"][i][j+1]):
                min = int(df4["light"][h])
                max = int(df4["light"][h]) + int(df4["range"][h])
                df["light"][i].append(min)
                df["light"][i].append(max)
                df["water_done"][i].append(df4["water"][h])
                df["water_done"][i].append(int(df4["water"][h]) + int(df4["range"][h]))
                df["new_range"][i] = df["new_range"][i] + max - min   

for i in range(0, len(df)):
    for j in range(0, len(df["water"][i]), 2):
        min = df["water"][i][j]
        max = df["water"][i][j+1]
        for k in range(0, len(df["water_done"][i]), 2):
            for l in range(0, len(df["water_done"][i]), 2):
                if min == df["water_done"][i][l] and min != df["water"][i][j+1]:
                    min = df["water_done"][i][l+1]
                if max == df["water_done"][i][l+1] and max != df["water"][i][j]:
                    max = df["water_done"][i][l]    

        if min != df["water"][i][j+1]:
            df["light"][i].append(min)
        if max != df["water"][i][j]:
            df["light"][i].append(max)
            df["new_range"][i] = df["new_range"][i] + max - min   
print(df)

df["new_range"] = 0                    

# temperature
for i in range(0, len(df)):
    for j in range(0, len(df["light"][i]), 2):
        for h in range(0, len(df5)):
            # both min and max in same range
            if int(df5["light"][h]) <= int(df["light"][i][j]) <= int(df5["light"][h]) + int(df5["range"][h]) \
                and int(df5["light"][h]) <= int(df["light"][i][j+1]) <= int(df5["light"][h]) + int(df5["range"][h]):
                min = int(df["light"][i][j]) + int(df5["temperature"][h]) - int(df5["light"][h])
                max = int(df["light"][i][j+1]) + int(df5["temperature"][h]) - int(df5["light"][h])
                df["temperature"][i].append(min)
                df["temperature"][i].append(max)
                df["light_done"][i].append(df["light"][i][j])
                df["light_done"][i].append(df["light"][i][j+1])
                df["new_range"][i] = df["new_range"][i] + max - min

            # min in range, but max out of range
            if int(df5["light"][h]) <= int(df["light"][i][j]) <= int(df5["light"][h]) + int(df5["range"][h]) \
                and int(df5["light"][h]) + int(df5["range"][h]) < int(df["light"][i][j+1]):
                min = int(df["light"][i][j]) + int(df5["temperature"][h]) - int(df5["light"][h])
                max = int(df5["temperature"][h]) + int(df5["range"][h])
                df["temperature"][i].append(min)
                df["temperature"][i].append(max)  
                df["light_done"][i].append(df["light"][i][j])
                df["light_done"][i].append(int(df5["light"][h]) + int(df5["range"][h]))
                df["new_range"][i] = df["new_range"][i] + max - min

            # # max in range, but min out of range
            if int(df["light"][i][j]) < int(df5["light"][h]) \
                and int(df5["light"][h]) <= int(df["light"][i][j+1]) <= int(df5["light"][h]) + int(df5["range"][h]):
                min = int(df5["temperature"][h])
                max = int(df["light"][i][j+1]) + int(df5["temperature"][h]) - int(df5["light"][h])
                df["temperature"][i].append(min)
                df["temperature"][i].append(max)
                df["light_done"][i].append(df5["light"][h])
                df["light_done"][i].append(df["light"][i][j+1])
                df["new_range"][i] = df["new_range"][i] + max - min

            # # min lower and max higher
            if int(df["light"][i][j]) < int(df5["light"][h]) \
                and int(df5["light"][h]) + int(df5["range"][h]) < int(df["light"][i][j+1]):
                min = int(df5["temperature"][h])
                max = int(df5["temperature"][h]) + int(df5["range"][h])
                df["temperature"][i].append(min)
                df["temperature"][i].append(max)
                df["light_done"][i].append(df5["light"][h])
                df["light_done"][i].append(int(df5["light"][h]) + int(df5["range"][h]))
                df["new_range"][i] = df["new_range"][i] + max - min      

for i in range(0, len(df)):
    for j in range(0, len(df["light"][i]), 2):
        min = df["light"][i][j]
        max = df["light"][i][j+1]
        for k in range(0, len(df["light_done"][i]), 2):
            for l in range(0, len(df["light_done"][i]), 2):
                if min == df["light_done"][i][l] and min != df["light"][i][j+1]:
                    min = df["light_done"][i][l+1]
                if max == df["light_done"][i][l+1] and max != df["light"][i][j]:
                    max = df["light_done"][i][l]    

        if min != df["light"][i][j+1]:
            df["temperature"][i].append(min)
        if max != df["light"][i][j]:
            df["temperature"][i].append(max)
            df["new_range"][i] = df["new_range"][i] + max - min   
print(df)

df["new_range"] = 0                    

# humidity
for i in range(0, len(df)):
    for j in range(0, len(df["temperature"][i]), 2):
        for h in range(0, len(df6)):
            # both min and max in same range
            if int(df6["temperature"][h]) <= int(df["temperature"][i][j]) <= int(df6["temperature"][h]) + int(df6["range"][h]) \
                and int(df6["temperature"][h]) <= int(df["temperature"][i][j+1]) <= int(df6["temperature"][h]) + int(df6["range"][h]):
                min = int(df["temperature"][i][j]) + int(df6["humidity"][h]) - int(df6["temperature"][h])
                max = int(df["temperature"][i][j+1]) + int(df6["humidity"][h]) - int(df6["temperature"][h])
                df["humidity"][i].append(min)
                df["humidity"][i].append(max)
                df["temperature_done"][i].append(df["temperature"][i][j])
                df["temperature_done"][i].append(df["temperature"][i][j+1])
                df["new_range"][i] = df["new_range"][i] + max - min

            # min in range, but max out of range
            if int(df6["temperature"][h]) <= int(df["temperature"][i][j]) <= int(df6["temperature"][h]) + int(df6["range"][h]) \
                and int(df6["temperature"][h]) + int(df6["range"][h]) < int(df["temperature"][i][j+1]):
                min = int(df["temperature"][i][j]) + int(df6["humidity"][h]) - int(df6["temperature"][h])
                max = int(df6["humidity"][h]) + int(df6["range"][h])
                df["humidity"][i].append(min)
                df["humidity"][i].append(max)  
                df["temperature_done"][i].append(df["temperature"][i][j])
                df["temperature_done"][i].append(int(df6["temperature"][h]) + int(df6["range"][h]))
                df["new_range"][i] = df["new_range"][i] + max - min

            # # max in range, but min out of range
            if int(df["temperature"][i][j]) < int(df6["temperature"][h]) \
                and int(df6["temperature"][h]) <= int(df["temperature"][i][j+1]) <= int(df6["temperature"][h]) + int(df6["range"][h]):
                min = int(df6["humidity"][h])
                max = int(df["temperature"][i][j+1]) + int(df6["humidity"][h]) - int(df6["temperature"][h])
                df["humidity"][i].append(min)
                df["humidity"][i].append(max)
                df["temperature_done"][i].append(df6["temperature"][h])
                df["temperature_done"][i].append(df["temperature"][i][j+1])
                df["new_range"][i] = df["new_range"][i] + max - min

            # # min lower and max higher
            if int(df["temperature"][i][j]) < int(df6["temperature"][h]) \
                and int(df6["temperature"][h]) + int(df6["range"][h]) < int(df["temperature"][i][j+1]):
                min = int(df6["humidity"][h])
                max = int(df6["humidity"][h]) + int(df6["range"][h])
                df["humidity"][i].append(min)
                df["humidity"][i].append(max)
                df["temperature_done"][i].append(df6["temperature"][h])
                df["temperature_done"][i].append(int(df6["temperature"][h]) + int(df6["range"][h]))
                df["new_range"][i] = df["new_range"][i] + max - min    

for i in range(0, len(df)):
    for j in range(0, len(df["temperature"][i]), 2):
        min = df["temperature"][i][j]
        max = df["temperature"][i][j+1]
        for k in range(0, len(df["temperature_done"][i]), 2):
            for l in range(0, len(df["temperature_done"][i]), 2):
                if min == df["temperature_done"][i][l] and min != df["temperature"][i][j+1]:
                    min = df["temperature_done"][i][l+1]
                if max == df["temperature_done"][i][l+1] and max != df["temperature"][i][j]:
                    max = df["temperature_done"][i][l]    

        if min != df["temperature"][i][j+1]:
            df["humidity"][i].append(min)
        if max != df["temperature"][i][j]:
            df["humidity"][i].append(max)
            df["new_range"][i] = df["new_range"][i] + max - min   
print(df)

df["new_range"] = 0      

# location
for i in range(0, len(df)):
    for j in range(0, len(df["humidity"][i]), 2):
        for h in range(0, len(df7)):
            # both min and max in same range
            if int(df7["humidity"][h]) <= int(df["humidity"][i][j]) <= int(df7["humidity"][h]) + int(df7["range"][h]) \
                and int(df7["humidity"][h]) <= int(df["humidity"][i][j+1]) <= int(df7["humidity"][h]) + int(df7["range"][h]):
                min = int(df["humidity"][i][j]) + int(df7["location"][h]) - int(df7["humidity"][h])
                max = int(df["humidity"][i][j+1]) + int(df7["location"][h]) - int(df7["humidity"][h])
                df["location"][i].append(min)
                df["humidity_done"][i].append(df["humidity"][i][j])
                df["humidity_done"][i].append(df["humidity"][i][j+1])
                df["new_range"][i] = df["new_range"][i] + max - min

            # min in range, but max out of range
            if int(df7["humidity"][h]) <= int(df["humidity"][i][j]) <= int(df7["humidity"][h]) + int(df7["range"][h]) \
                and int(df7["humidity"][h]) + int(df7["range"][h]) < int(df["humidity"][i][j+1]):
                min = int(df["humidity"][i][j]) + int(df7["location"][h]) - int(df7["humidity"][h])
                max = int(df7["location"][h]) + int(df7["range"][h])
                df["location"][i].append(min)
                df["humidity_done"][i].append(df["humidity"][i][j])
                df["humidity_done"][i].append(int(df7["humidity"][h]) + int(df7["range"][h]))
                df["new_range"][i] = df["new_range"][i] + max - min

            # # max in range, but min out of range
            if int(df["humidity"][i][j]) < int(df7["humidity"][h]) \
                and int(df7["humidity"][h]) <= int(df["humidity"][i][j+1]) <= int(df7["humidity"][h]) + int(df7["range"][h]):
                min = int(df7["location"][h])
                max = int(df["humidity"][i][j+1]) + int(df7["location"][h]) - int(df7["humidity"][h])
                df["location"][i].append(min)
                df["humidity_done"][i].append(df7["humidity"][h])
                df["humidity_done"][i].append(df["humidity"][i][j+1])
                df["new_range"][i] = df["new_range"][i] + max - min

            # # min lower and max higher
            if int(df["humidity"][i][j]) < int(df7["humidity"][h]) \
                and int(df7["humidity"][h]) + int(df7["range"][h]) < int(df["humidity"][i][j+1]):
                min = int(df7["location"][h])
                max = int(df7["location"][h]) + int(df7["range"][h])
                df["location"][i].append(min)
                df["humidity_done"][i].append(df7["humidity"][h])
                df["humidity_done"][i].append(int(df7["humidity"][h]) + int(df7["range"][h]))
                df["new_range"][i] = df["new_range"][i] + max - min                                 

for i in range(0, len(df)):
    for j in range(0, len(df["humidity"][i]), 2):
        min = df["humidity"][i][j]
        max = df["humidity"][i][j+1]
        for k in range(0, len(df["humidity_done"][i]), 2):
            for l in range(0, len(df["humidity_done"][i]), 2):
                if min == df["humidity_done"][i][l] and min != df["humidity"][i][j+1]:
                    min = df["humidity_done"][i][l+1]
                if max == df["humidity_done"][i][l+1] and max != df["humidity"][i][j]:
                    max = df["humidity_done"][i][l]    

        if min != df["humidity"][i][j+1]:
            df["location"][i].append(min)
        if max != df["humidity"][i][j]:
            df["location"][i].append(max)
            df["new_range"][i] = df["new_range"][i] + max - min   

for i in range(len(df)):
    for j in range(len(df["location"][i])):
        if j == 0:
            df["min"][i] = df["location"][i][j]
        else:
            if df["location"][i][j] < df["min"][i]:
                df["min"][i] = df["location"][i][j]

print(df)

# print(df["location"])
# print(min)