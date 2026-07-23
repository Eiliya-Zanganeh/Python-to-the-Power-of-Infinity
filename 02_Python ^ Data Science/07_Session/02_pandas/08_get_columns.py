import pandas as pd

df = pd.DataFrame({
    'Name': ["Ali", "Bob", "Charlie", "David"],
    'Age': [60, 20, 33, 42],
    'Score': [20, 18, 17, 18],
    'City': ['Tehran', "Esfahan", "Mashhad", "Shiraz"]
})

# print(df['Score'])
print(type(df[['Name', 'Age']]))