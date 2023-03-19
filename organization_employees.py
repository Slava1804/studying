# https://stepik.org/lesson/571244/step/5?unit=565785

from datetime import date, datetime

n = int(input())

person_data = {
    d[:-11]: datetime.strptime(d[-10:], '%d.%m.%Y')
    for d in (input() for _ in range(n))
}

largest = min(person_data.values())
count = 0

for key, value in person_data.items():
    if value == largest:
        count += 1
        name = key

if count > 1:
    print(largest.strftime('%d.%m.%Y'), count)
else:
    print(largest.strftime('%d.%m.%Y'), name)