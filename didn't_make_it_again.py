# https://stepik.org/lesson/571244/step/3?unit=565785

from datetime import date, time, datetime, timedelta

d = datetime.strptime(input(), '%d.%m.%Y %H:%M') 
t = timedelta(hours=d.hour, minutes=d.minute)

if d.weekday() < 5 and timedelta(hours=9) <= t < timedelta(hours=21):
    print(int((timedelta(hours=21)-t).total_seconds()//60))
elif d.weekday() > 5 and timedelta(hours=10) <= t < timedelta(hours=18):
    print(int((timedelta(hours=18)-t).total_seconds()//60))
else:
    print('Магазин не работает')