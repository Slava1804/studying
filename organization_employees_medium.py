# https://stepik.org/lesson/571244/step/6?unit=565785

from datetime import date, datetime

person_data = {}
pattern = '%d.%m.%Y'

for _ in range(int(input())):
    d = input()
    key = datetime.strptime(d[-10:], pattern)
    person_data[key] = person_data.get(key, 0) + 1

largest = max(person_data.values())

for k, v in sorted(person_data.items()):
    if v == largest:
        print(k.strftime(pattern))