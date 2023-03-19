# https://stepik.org/lesson/518491/step/18?unit=510939

import csv

with open('titanic.csv', encoding='utf-8') as file:
    data = list(csv.reader(file, delimiter=';'))
    del data[0]

    sort_data = filter(lambda x: float(x[-1]) < 18 and int(x[0]), data)

    for person in sorted(sort_data, key=lambda x: x[2], reverse=True):
        print(person[1])