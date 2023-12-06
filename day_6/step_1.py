import pandas as pd

df = pd.DataFrame([[46, 347], [82, 1522], [84, 1406], [79, 1471]], columns=["time", "distance"])
df["possible"] = 0

for i in range(0, len(df)):
    print(df["time"][i])
    for j in range(0, df["time"][i]):
        if j * (df["time"][i] - j) > df["distance"][i]:
            df["possible"][i] = df["possible"][i] + 1
            print(j * df["time"][i] - j)

product = df["possible"].product()
print(df)
print(product)