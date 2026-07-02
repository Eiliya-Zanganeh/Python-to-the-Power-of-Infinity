students = [
    {
        'name': 'ali',
        'family': 'ahmadi',
        'scores': [20, 18, 17, 16]
    },
    {
        'name': 'mohammad',
        'family': 'zanganeh',
        'scores': [18, 18.25, 17, 16]
    },
    {
        'name': 'taha',
        'family': 'asadi',
        'scores': [20, 18, 17.5, 20]
    },
]

for student in students:
    total = 0

    for score in student['scores']:
        total += score

    print(total / len(student['scores']))



