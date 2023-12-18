import pandas as pd

df = pd.read_csv("day_10/input.csv", names=["all"])

start_row = df.index[df["all"].str.find("S") > -1][0]
start_position = df["all"][start_row].find("S")
if df["all"][start_row-1][start_position:start_position+1] in ["|", "F", "7"] :
    row = start_row - 1
    position = start_position
    sign = df["all"][start_row-1][start_position:start_position+1]
    direction = "up"
elif df["all"][start_row+1][start_position:start_position+1] in ["|" ,"L", "J"]:
    row = start_row + 1
    position = start_position    
    sign = df["all"][start_row+1][start_position:start_position+1]
    direction = "down"
elif df["all"][start_row][start_position+1:start_position+2] in ["-" ,"L", "J"]:
    row = start_row
    position = start_position +1  
    sign = df["all"][start_row][start_position+1:start_position+2]
    direction = "right"
elif df["all"][start_row][start_position-1:start_position] in ["-" ,"L", "J"]:
    row = start_row
    position = start_position -1      
    sign = df["all"][start_row][start_position-1:start_position]
    direction = "left"

steps = 1
while sign != "S":
    if sign == "|":
        if direction == "up":
            row = row - 1
            position = position
            sign = df["all"][row][position:position+1]
            direction = "up"
        else:
            row = row + 1
            position = position
            sign = df["all"][row][position:position+1]
            direction = "down"       
    elif sign == "F":
        if direction == "up":
            row = row
            position = position + 1
            sign = df["all"][row][position:position+1]
            direction = "right"
        else:
            row = row + 1
            position = position
            sign = df["all"][row][position:position+1]
            direction = "down"  
    elif sign == "7":
        if direction == "up":
            row = row
            position = position - 1
            sign = df["all"][row][position:position+1]
            direction = "left"
        else:
            row = row + 1
            position = position
            sign = df["all"][row][position:position+1]
            direction = "down"        
    elif sign == "L":
        if direction == "left":
            row = row - 1
            position = position
            sign = df["all"][row][position:position+1]
            direction = "up"
        else:
            row = row
            position = position + 1
            sign = df["all"][row][position:position+1]
            direction = "right"
    elif sign == "J":
        if direction == "right":
            row = row - 1
            position = position
            sign = df["all"][row][position:position+1]
            direction = "up"
        else:
            row = row
            position = position - 1
            sign = df["all"][row][position:position+1]
            direction = "left"          
    elif sign == "-":
        if direction == "right":
            row = row
            position = position + 1
            sign = df["all"][row][position:position+1]
            direction = "right"
        else:
            row = row
            position = position - 1
            sign = df["all"][row][position:position+1]
            direction = "left"   

    steps += 1
    print(f"step {steps} given sign {sign}")

print(steps/2)
