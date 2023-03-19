# https://stepik.org/lesson/518491/step/22?unit=510939

import csv

with open('prices.csv', encoding='utf-8') as file:
    data = csv.DictReader(file, delimiter=';')
    smallest = ('яя', 999)

    for row in data:
        obj = list(row.items())
        sl = min(obj[1:], key=lambda x: (int(x[1]), x[0]))
        
        if (int(sl[1]), sl[0]) < (int(smallest[1]), smallest[0]):
            shop = obj[0][1]
            smallest = sl

    print(f'{smallest[0]}: {shop}')