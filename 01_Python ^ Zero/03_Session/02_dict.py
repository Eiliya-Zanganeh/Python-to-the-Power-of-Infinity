data = {
    # 'users': ['Eiliya', 'Ali', 'Sara'],
    'registry': 1997,
    'is_open': True,
    'description': 'description'
}

# print(data['users'])

# print(data.get('users'))
#
# print(data.keys())
# print(data.values())
# print(data.items())

contacts = {
    'Eiliya': "09056598570",
    'Ali': "09056598571",
    'Sara': "09056598572"
}

# print("09056598570" in contacts.values())
# print("Eiliya" in contacts.keys())

# outputs = []
# for num in range(10):
#     outputs.append(num ** 2)

# outputs = [num ** 2 for num in range(10)]
# print(outputs)

# outputs = {}
# for num in range(10):
#     outputs[f"num_{num}"] = num ** 2

outputs = {f"num_{num}": num ** 2 for num in range(10)}
print(outputs)
