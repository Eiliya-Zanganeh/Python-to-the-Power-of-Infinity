import json

with open('data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

data['friends'] = 'Ahmad'

with open('data.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, indent=4)