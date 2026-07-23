import pandas as pd

df = pd.DataFrame({
    'Name': ["Ali", "Bob", "Charlie", "David"],
    'Age': [60, 20, 33, 42],
    'Score': [20, 18, 17, 18],
    'City': ['Tehran', "Esfahan", "Mashhad", "Shiraz"]
})

# print(df['Age'] > 30)
# print(df[df['Age'] > 30])

# mashhad_students = df[df['City'] == 'Mashhad']
# scores_mashhad_students = mashhad_students['Score']
# print(scores_mashhad_students.values)

# print(df[(df['City'] == 'Mashhad') & (df['Score'] >= 17)])
# print(df[(df['City'] == 'Mashhad') | (df['Score'] >= 17)])
# print(df[df['City'] == 'Mashhad'])

filtred_data = df[df['Score'] > 17]['Score'].values
print(filtred_data.mean())
print(filtred_data.max())
print(filtred_data.min())
print(filtred_data.sum())
print(filtred_data.std())
