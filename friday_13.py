# https://stepik.org/lesson/571244/step/2?unit=565785

from datetime import date, time, datetime, timedelta

start, end = date(year=1, month=1, day=1), date(year=9999, month=12, day=31)
dict_days = {k: 0 for k in range(7)}

for day in range(start.toordinal(), end.toordinal()+1):
    if datetime.fromordinal(day).day == 13:
        dict_days[datetime.fromordinal(day).weekday()] += 1

print(*dict_days.values(), sep='\n')