import json
from pathlib import Path

BASE_PATH = Path.cwd().joinpath('tests','data')

def reader(file_name):
    path = get_file_with_json(file_name)
    
    with path.open(mode='r', encoding="utf-8") as f:
        return json.load(f)

def get_file_with_json(file_name):
    if '.json' in file_name:
        path = BASE_PATH.joinpath(file_name)
    else:
        path = BASE_PATH.joinpath(f'{file_name}.json')
    return path
