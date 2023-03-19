# https://stepik.org/lesson/518491/step/21?unit=510939

import csv

with open('student_counts.csv', encoding='utf-8') as file:
    data = csv.DictReader(file, delimiter=',')
    columns = ['year'] + sorted(data.fieldnames[1:], key=lambda x: (int(x.split('-')[0]), x.split('-')[1]))
    result = list(data)

with open('sorted_student_counts.csv', 'w', encoding='utf-8', newline='') as file_res:
    writer = csv.DictWriter(file_res, fieldnames=columns, delimiter=',')
    writer.writeheader()
    writer.writerows(result)