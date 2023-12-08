import pandas as pd

example = "LLR"
input = "LRRRLRRLLLRRRLRLRRLRRRLRLRRRLLLRRLRRLRRRLRRRLRLLRLRRLRRLLRRLRLRRRLRRLRRLRRLLRRRLRLRLRLRLLRRLLLRRLRLRRLRLLLLRRLRRRLRRLRRRLLRRRLRRLRRRLRLLRLRRLRRLLRRRLLLRLRRRLLLRRLLRRRLLRRLRRLRRLRLRRRLLRRRLRLLRLRRLLRLRRLRLLRLRRLRRRLLRRLLRRRLRRLRLRLRRRLRLRRRLRRRLRRLRRRLRLLRRRLLRRRR"
sequence = input
length = len(sequence)
df  = pd.read_csv("day_8/input.csv", delimiter=" = ", engine='python')
df["L"] = df["rightleft"].str.slice(1,4)
df["R"] = df["rightleft"].str.slice(6,9)

steps = 0
current = "AAA"

while current != "ZZZ":
    # zoek naar current in df current
    # vind daar rij nummer
    index = df.index[df["current"] == current].to_list()
    # bepaal of je links of rechts moet gaan en vind daar de nieuwe waarde van
    current = df[f"{sequence[(steps % length): (steps % length) + 1]}"][index[0]]
    # stapje omhoog
    steps+=1

print(steps)
