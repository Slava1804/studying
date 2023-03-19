# https://stepik.org/lesson/623073/step/9?unit=618703

import json

with open('people.json', encoding='utf-8') as file:
    data = json.load(file)
    data_keys = set()

    for d in data:
        data_keys.update(d.keys())

    for dict_people in data:
        if set(dict_people.keys()) != data_keys:
            for key in data_keys:
                dict_people.setdefault(key, None)

with open('updated_people.json', 'w') as file:
    json.dump(data, file)