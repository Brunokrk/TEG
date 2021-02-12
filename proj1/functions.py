
from json import load


def open_json():
    with open('entrada.json', 'r') as json_file:
        data = load(json_file)
    return data
