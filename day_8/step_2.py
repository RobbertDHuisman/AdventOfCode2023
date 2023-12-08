import pandas as pd

example = "LR"
input = "LRRRLRRLLLRRRLRLRRLRRRLRLRRRLLLRRLRRLRRRLRRRLRLLRLRRLRRLLRRLRLRRRLRRLRRLRRLLRRRLRLRLRLRLLRRLLLRRLRLRRLRLLLLRRLRRRLRRLRRRLLRRRLRRLRRRLRLLRLRRLRRLLRRRLLLRLRRRLLLRRLLRRRLLRRLRRLRRLRLRRRLLRRRLRLLRLRRLLRLRRLRLLRLRRLRRRLLRRLLRRRLRRLRLRLRRRLRLRRRLRRRLRRLRRRLRLLRRRLLRRRR"
sequence = input
length = len(sequence)
# df  = pd.read_csv("day_8/example2.csv", delimiter=" = ", engine='python')
df  = pd.read_csv("day_8/input.csv", delimiter=" = ", engine='python')
df["L"] = df["rightleft"].str.slice(1,4)
df["R"] = df["rightleft"].str.slice(6,9)

steps = 0
df_A = df[df["current"].str.rfind('') == 2]["current"].reset_index()
total_number = len(df_A)
number_z = 0
current = df_A["current"][0]

while number_z != "Z":
    rows = df["current"] == current
    columns = sequence[(steps % length): (steps % length) + 1]
    current = df.loc[rows, [columns]].reset_index()[columns][0]    
    # stapje omhoog
    steps+=1    
    number_z = current[2:3]
    print(number_z)
    print(steps)
    print(current)




# while number_z != total_number:
# # for i in range(0,2):
#     for i in range(0, len(df_A)):
#     # for i in range(0, 2):
#         # zoek naar current in df current
#         # vind daar rij nummer
#         # index = df.loc[df["current"] == df_A["current"][i]]
#         # bepaal of je links of rechts moet gaan en vind daar de nieuwe waarde van
#         rows = df["current"] == df_A["current"][i]
#         columns = sequence[(steps % length): (steps % length) + 1]
#         df_A["current"][i] = df.loc[rows, [columns]].reset_index()[columns][0]

#     # bepaal nieuw aantal Z's aan het einde
#     number_z = len(df_A[df_A["current"].str.rfind('Z') == 2])
#     # stapje omhoog
#     steps+=1
#     print(steps)

# print(steps)
