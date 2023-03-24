# https://stepik.org/lesson/623073/step/14?thread=solutions&unit=618703

import csv, json
from datetime import datetime

with open('exam_results.csv', encoding='utf-8') as file:
    data = list(csv.DictReader(file))
    students = {}
    keys = list(data[0].keys())[3:]
    result = []

    for info in data:
        key = info['name']+' '+info['surname']
        date = datetime.strptime(info['date_and_time'], '%Y-%m-%d %H:%M:%S')
        if key in students:
            if int(students[key]['best_score']) <= int(info['score']):
                students[key]['best_score'] = int(info['score'])
                if date > datetime.strptime(students[key]['date_and_time'], '%Y-%m-%d %H:%M:%S'):
                    students[key]['date_and_time'] = info['date_and_time']
        else:
            students[key] = students.get(key, dict(zip(keys, list(info.values())[3:])))
            students[key]['best_score'] = int(info['score'])

    for student in students:
        d = {}
        name, surname = student.split()
        d['name'] = name
        d['surname'] = surname
        d['best_score'] = students[student]['best_score']
        d['date_and_time'] = students[student]['date_and_time']
        d['email'] = students[student]['email']
        result.append(d)

    result.sort(key=lambda x: x['email'])

with open('best_scores.json', 'w', encoding='utf-8') as file:
    json.dump(result, file, indent=2)