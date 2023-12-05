import pandas as pd

df  = pd.read_csv("day_5/seeds.csv")
df1 = pd.read_csv("day_5/seed_to_soil.csv", delimiter=" ")
df2 = pd.read_csv("day_5/soil_to_fertilizer.csv", delimiter=" ")
df3 = pd.read_csv("day_5/fertilizer_to_water.csv", delimiter=" ")
df4 = pd.read_csv("day_5/water_to_light.csv", delimiter=" ")
df5 = pd.read_csv("day_5/light_to_temperature.csv", delimiter=" ")
df6 = pd.read_csv("day_5/temperature_to_humidity.csv", delimiter=" ")
df7 = pd.read_csv("day_5/humidity_to_location.csv", delimiter=" ")

df["soil"] = pd.Series([[] for i in range(1)])
df["fertilizer"] = pd.Series([[] for i in range(1)])
df["water"] = pd.Series([[] for i in range(1)])
df["light"] = pd.Series([[] for i in range(1)])
df["temperature"] = pd.Series([[] for i in range(1)])
df["humidity"] = pd.Series([[] for i in range(1)])
df["location"] = pd.Series([[] for i in range(1)])
df["seeds"] = df["seeds"].str.split(pat=" ")
# soil
for i in range(0, len(df["seeds"][0])):
    for j in range(0, len(df1)):
        if int(df1["seed"][j]) <= int(df["seeds"][0][i]) <= int(df1["seed"][j]) + int(df1["range"][j]):
            df["soil"][0].append(int(df["seeds"][0][i]) + int(df1["soil"][j]) - int(df1["seed"][j]))

# fertilizer
for i in range(0, len(df["soil"][0])):
    for j in range(0, len(df2)):
        if int(df2["soil"][j]) <= int(df["soil"][0][i]) <= int(df2["soil"][j]) + int(df2["range"][j]):
            df["fertilizer"][0].append(int(df["soil"][0][i]) + int(df2["fertilizer"][j]) - int(df2["soil"][j]))   

# water
for i in range(0, len(df["fertilizer"][0])):
    for j in range(0, len(df3)):
        if int(df3["fertilizer"][j]) <= int(df["fertilizer"][0][i]) <= int(df3["fertilizer"][j]) + int(df3["range"][j]):
            df["water"][0].append(int(df["fertilizer"][0][i]) + int(df3["water"][j]) - int(df3["fertilizer"][j]))                        

# light
for i in range(0, len(df["water"][0])):
    for j in range(0, len(df4)):
        if int(df4["water"][j]) <= int(df["water"][0][i]) <= int(df4["water"][j]) + int(df4["range"][j]):
            df["light"][0].append(int(df["water"][0][i]) + int(df4["light"][j]) - int(df4["water"][j]))    

# temperature
for i in range(0, len(df["light"][0])):
    for j in range(0, len(df5)):
        if int(df5["light"][j]) <= int(df["light"][0][i]) <= int(df5["light"][j]) + int(df5["range"][j]):
            df["temperature"][0].append(int(df["light"][0][i]) + int(df5["temperature"][j]) - int(df5["light"][j]))     

# humidity
for i in range(0, len(df["temperature"][0])):
    for j in range(0, len(df6)):
        if int(df6["temperature"][j]) <= int(df["temperature"][0][i]) <= int(df6["temperature"][j]) + int(df6["range"][j]):
            df["humidity"][0].append(int(df["temperature"][0][i]) + int(df6["humidity"][j]) - int(df6["temperature"][j]))  

# location
for i in range(0, len(df["humidity"][0])):
    for j in range(0, len(df7)):
        if int(df7["humidity"][j]) <= int(df["humidity"][0][i]) <= int(df7["humidity"][j]) + int(df7["range"][j]):
            df["location"][0].append(int(df["humidity"][0][i]) + int(df7["location"][j]) - int(df7["humidity"][j]))                                        

min = min(df["location"][0])
print(df["location"])
print(min)