# https://stepik.org/lesson/518491/step/19?unit=510939

import csv
from datetime import datetime

with open('name_log.csv', encoding='utf-8') as file:
    data = list(csv.reader(file, delimiter=','))
    del data[0]
    dict_users = {}

    for name, email, dtime in data:
        t = datetime.strptime(dtime, '%d/%m/%Y %H:%M')
        dict_users[email] = dict_users.get(email, []) + [name, t]

    result = []
    columns = ['username', 'email', 'dtime']

    for inf in sorted(dict_users.items()):
        el = {}
        larg = max(c for c in inf[1] if isinstance(c, datetime))
        el['username'] = inf[1][inf[1].index(larg) - 1]
        el['email'] = inf[0]
        el['dtime'] = datetime.strftime(larg, '%d/%m/%Y %H:%M')
        result.append(el)

with open('new_name_log.csv', 'w', encoding='utf-8', newline='') as file_res:
    writer = csv.DictWriter(file_res, fieldnames=columns, delimiter=',')
    writer.writeheader()
    writer.writerows(result)