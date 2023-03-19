# https://stepik.org/lesson/571244/step/4?unit=565785

from datetime import datetime, date

start, end = [datetime.strptime(input(), '%d.%m.%Y').toordinal() for _ in range(2)]

for dat in range(start, end+1):
    d = date.fromordinal(dat)
    s = sum(map(int, d.strftime('%m %d').split()))
    if s % 2 != 0:
        start = d.toordinal()
        break


for d in range(start, end+1, 3):
    w = date.fromordinal(d).weekday()
    if w != 0 and w != 3:
        print(date.fromordinal(d).strftime('%d.%m.%Y'))