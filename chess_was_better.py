# https://stepik.org/lesson/547172/step/22?unit=540798

from zipfile import ZipFile
import json

def is_correct_json(string):
    try:
        json.loads(string)
        return True
    except:
        return False

with ZipFile('data.zip') as file:
    files = file.infolist()
    result = []

    for f in files:
        if is_correct_json(json.dumps(f.filename)) and not f.is_dir():
            try:
                with file.open(f.filename) as file_j:
                    result.append(json.load(file_j))
            except:
                continue

for inf in sorted(result, key=lambda x: (x['first_name'], x['last_name'])):
    if inf['team'] == 'Arsenal':
        print(inf['first_name'], inf['last_name'])