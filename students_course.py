# https://stepik.org/lesson/623073/step/12?unit=618703

import json
import csv

with open('students.json', encoding='utf-8') as file:
    data = json.load(file)
    result = []

    for d in data:
        if d['age'] >= 18 and d['progress'] >= 75:
            result.append([d['name'], d['phone']])

with open('data.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['name', 'phone'])
    writer.writerows(sorted(result))