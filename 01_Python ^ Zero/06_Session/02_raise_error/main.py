import json

def read_json(file_path):
    if file_path.endswith('.json'):
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    else:
        raise ValueError(f"File format not supported! please define json file")

print(read_json('main.txt'))