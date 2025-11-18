import json
import os

def load_data(path):
    if not os.path.exists(path):
        return []

    try:
        with open(path, mode='r', encoding='utf-8') as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []

def save_data(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)

    with open(path, mode='w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)