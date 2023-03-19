# https://stepik.org/lesson/623073/step/11?unit=618703

import json
import csv

with open('playgrounds.csv', encoding='utf-8') as file:
    data = csv.DictReader(file, delimiter=';')
    result = {}
    
    for d in data:
        result.setdefault(d['AdmArea'], {}).setdefault(d['District'], []).append(d['Address'])

with open('addresses.json', 'w', encoding='utf-8') as file:
    json.dump(result, file, ensure_ascii=False)