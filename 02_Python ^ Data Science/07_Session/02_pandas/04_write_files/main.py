import pandas as pd

students = pd.DataFrame(
    {
        'Name': ['Sara', 'Amir', "Hesam"],
        "Age": [18, 22, 21],
        'score': [18, 20, 17]
    }
)

students.to_csv('students.csv', index=False)
students.to_excel('students.xlsx')
