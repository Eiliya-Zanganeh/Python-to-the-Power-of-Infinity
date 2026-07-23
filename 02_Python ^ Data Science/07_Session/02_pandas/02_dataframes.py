import pandas as pd

students = pd.DataFrame(
    {
        'Name': ['Sara', 'Amir', "Hesam"],
        "Age": [18, 22, 21],
        'score': [18, 20, 17]
    }
)

print(students)
