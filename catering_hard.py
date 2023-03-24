# https://stepik.org/lesson/623073/step/16?unit=618703

import json

with open('food_services.json', encoding='utf-8') as file:
    data = json.load(file)

    services = {}
    for row in data:
        services[row['TypeObject']] = services.get(row['TypeObject'], {})
        services[row['TypeObject']][(row['Name'], row['Address'])] = row['SeatsCount']

    for key, value in sorted(services.items()):
        name, count = max(value.items(), key=lambda x: x[1])
        print(f'{key}: {name[0]}, {count}')