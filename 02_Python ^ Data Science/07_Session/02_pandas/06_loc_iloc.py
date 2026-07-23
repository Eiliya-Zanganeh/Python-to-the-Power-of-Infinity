import pandas as pd

df = pd.DataFrame({
    'Name': ["Ali", "Bob", "Charlie", "David"],
    'Age': [60, 20, 33, 42],
    'Score': [20, 18, 17, 18],
    'City': ['Tehran', "Esfahan", "Mashhad", "Shiraz"]
})
# print(df.iloc[0:2, :])

# df.index = [101, 102, 103, 104]
# print(df.loc[0])
# print(df.iloc[0])

# print(df.loc[0:3, ['Name', "Age"]])
# print(df.iloc[0:4, :])