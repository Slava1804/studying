# https://stepik.org/lesson/740203/step/12?thread=solutions&unit=741843

from collections import namedtuple
from datetime import datetime
import csv

with open('meetings.csv', encoding='utf-8') as file:
    _, *data = csv.reader(file)
    guests = []
    Guest = namedtuple('Guest', 'name time')

    for name, surname, date, time in data:
        guest, time_meet = f'{name} {surname}', datetime.strptime(f'{date} {time}', '%d.%m.%Y %H:%M')
        guests.append(Guest(guest, time_meet))

    for person in sorted(guests, key=lambda x: x.time):
        print(person.name)