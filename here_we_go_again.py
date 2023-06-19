# https://stepik.org/lesson/635441/step/18?thread=solutions&unit=631831

from collections import Counter
import csv

with open('name_log.csv', encoding='utf-8') as file:
    rows = list(csv.reader(file))[1:]
    result = Counter(email for _, email, _ in rows)

    for email, count in sorted(result.items()):
        print(f'{email}: {count}')