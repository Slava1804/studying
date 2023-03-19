# https://stepik.org/lesson/623073/step/13?unit=618703

import json

with open('pools.json', encoding='utf-8') as file:
    data = json.load(file)
    pool = []

    for d in data:
        start, end = d['WorkingHoursSummer']['Понедельник'].split('-')
        if int(start.split(':')[0]) <= 10 and int(end.split(':')[0]) >= 12:
            info_pool = d['DimensionsSummer']
            pool.append([info_pool['Length'], info_pool['Width'], d['Address']])

    largest_pool = max(pool, key=lambda x: (x[0], x[1]))
    print(f'{largest_pool[0]}x{largest_pool[1]}\n{largest_pool[2]}')