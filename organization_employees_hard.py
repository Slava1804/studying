# https://stepik.org/lesson/571244/step/7?unit=565785

from datetime import datetime, timedelta

br = datetime.strptime(input(), '%d.%m.%Y')
n = int(input())
res = ''
smallest = datetime(1, 1, 1)

for _ in range(n):
    person = input()
    name, date_brht = person[:-11], datetime.strptime(person[-10:], '%d.%m.%Y')
    if smallest < date_brht and (
            br < date_brht.replace(year=br.year) < br + timedelta(days=8) or
            br < date_brht.replace(year=br.year + 1) < br + timedelta(days=8)):
        res = name
        smallest = date_brht

print([res, 'Дни рождения не планируются'][res == ''])