import pandas as pd

students = pd.DataFrame(
    {
        'Name': ['Sara', 'Amir', "Hesam"],
        "Age": [18, 22, 21],
        'score': [18, 20, 17]
    }
)
# print(students.head(1))
# print(students.tail(1))
# print(students.shape)
# print(students.info())
# print(students.describe())
# students.columns = ['1', '2', '3']
# print(students.columns)
# print(students.index)
print(students.dtypes)